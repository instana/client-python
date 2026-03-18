#!/bin/bash

# =============================================================================
# INSTANA PYTHON SDK PYPI PUBLISHING SCRIPT
# =============================================================================
# This script handles publishing the SDK to PyPI
# =============================================================================

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"
PYPI_USERNAME="${PYPI_USERNAME:-__token__}"
PYPI_PASSWORD="${PYPI_PASSWORD:-}"
PYPI_REPOSITORY="${PYPI_REPOSITORY:-pypi}"
DRY_RUN="${DRY_RUN:-false}"

# Function to print colored output
print_header() {
    echo -e "\n${CYAN}========================================${NC}"
    echo -e "${CYAN}$1${NC}"
    echo -e "${CYAN}========================================${NC}\n"
}

print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Function to show usage
show_usage() {
    cat << EOF
Usage: $0 [OPTIONS]

Publish Instana Python SDK to PyPI

OPTIONS:
    -u, --username USER         PyPI username (default: __token__)
    -p, --password PASS         PyPI password/token (required)
    -r, --repository REPO       PyPI repository (default: pypi, use testpypi for testing)
    -d, --dry-run              Check packages without uploading
    -h, --help                 Show this help message

EXAMPLES:
    # Publish to PyPI with token
    $0 --password YOUR_PYPI_TOKEN

    # Publish to Test PyPI
    $0 --password YOUR_TEST_TOKEN --repository testpypi

    # Dry run to check packages
    $0 --dry-run

    # Publish with username/password (legacy)
    $0 --username myuser --password mypassword

ENVIRONMENT VARIABLES:
    PYPI_USERNAME             PyPI username (default: __token__)
    PYPI_PASSWORD             PyPI password/token
    PYPI_REPOSITORY           PyPI repository (default: pypi)

NOTES:
    - For PyPI API tokens, use username: __token__
    - Get tokens at: https://pypi.org/manage/account/token/
    - Test PyPI: https://test.pypi.org/manage/account/token/

EOF
}

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -u|--username)
            PYPI_USERNAME="$2"
            shift 2
            ;;
        -p|--password)
            PYPI_PASSWORD="$2"
            shift 2
            ;;
        -r|--repository)
            PYPI_REPOSITORY="$2"
            shift 2
            ;;
        -d|--dry-run)
            DRY_RUN=true
            shift
            ;;
        -h|--help)
            show_usage
            exit 0
            ;;
        *)
            print_error "Unknown option: $1"
            show_usage
            exit 1
            ;;
    esac
done

# Change to project root
cd "$PROJECT_ROOT"

print_header "Instana Python SDK PyPI Publishing"
print_status "Project root: $PROJECT_ROOT"
print_status "Repository: $PYPI_REPOSITORY"
print_status "Username: $PYPI_USERNAME"
print_status "Dry run: $DRY_RUN"

# =============================================================================
# STEP 1: Validate prerequisites
# =============================================================================
print_header "Step 1: Validating prerequisites"

# Check if dist directory exists
if [ ! -d "dist" ]; then
    print_error "dist/ directory not found"
    print_status "Run './automation/update_sdk.sh' first to build packages"
    exit 1
fi

# Check if packages exist
PACKAGE_COUNT=$(ls -1 dist/*.whl dist/*.tar.gz 2>/dev/null | wc -l)
if [ "$PACKAGE_COUNT" -eq 0 ]; then
    print_error "No distribution packages found in dist/"
    print_status "Run './automation/update_sdk.sh' first to build packages"
    exit 1
fi

print_success "Found $PACKAGE_COUNT distribution package(s)"
ls -lh dist/

# Get version from package
CURRENT_VERSION=$(grep "^VERSION = " setup.py | sed 's/VERSION = "\(.*\)"/\1/')
print_status "SDK version: $CURRENT_VERSION"

# =============================================================================
# STEP 2: Setup publishing environment
# =============================================================================
print_header "Step 2: Setting up publishing environment"

if [ "$DRY_RUN" = false ]; then
    # Create virtual environment for publishing
    print_status "Creating virtual environment..."
    python3 -m venv .venv-publish
    source .venv-publish/bin/activate
    
    # Install twine
    print_status "Installing twine..."
    pip install --upgrade twine
    
    print_success "Publishing environment ready"
else
    print_status "DRY RUN: Would create virtual environment and install twine"
fi

# =============================================================================
# STEP 3: Check packages
# =============================================================================
print_header "Step 3: Checking packages"

if [ "$DRY_RUN" = false ]; then
    source .venv-publish/bin/activate
    
    print_status "Running twine check..."
    if twine check dist/*; then
        print_success "Package check passed"
    else
        print_error "Package check failed"
        deactivate
        rm -rf .venv-publish
        exit 1
    fi
else
    print_status "DRY RUN: Would run twine check on packages"
fi

# =============================================================================
# STEP 4: Upload to PyPI
# =============================================================================
if [ "$DRY_RUN" = false ]; then
    print_header "Step 4: Uploading to PyPI"
    
    # Validate credentials
    if [ -z "$PYPI_PASSWORD" ]; then
        print_error "PyPI password/token is required"
        print_status "Use --password option or set PYPI_PASSWORD environment variable"
        deactivate
        rm -rf .venv-publish
        exit 1
    fi
    
    source .venv-publish/bin/activate
    
    print_status "Uploading packages to $PYPI_REPOSITORY..."
    print_status "This may take a moment..."
    
    # Upload to PyPI
    if [ "$PYPI_REPOSITORY" = "pypi" ]; then
        twine upload dist/* -u "$PYPI_USERNAME" -p "$PYPI_PASSWORD"
        PACKAGE_URL="https://pypi.org/project/instana-client/$CURRENT_VERSION/"
    elif [ "$PYPI_REPOSITORY" = "testpypi" ]; then
        twine upload --repository testpypi dist/* -u "$PYPI_USERNAME" -p "$PYPI_PASSWORD"
        PACKAGE_URL="https://test.pypi.org/project/instana-client/$CURRENT_VERSION/"
    else
        twine upload --repository "$PYPI_REPOSITORY" dist/* -u "$PYPI_USERNAME" -p "$PYPI_PASSWORD"
        PACKAGE_URL="Custom repository: $PYPI_REPOSITORY"
    fi
    
    print_success "Successfully uploaded to $PYPI_REPOSITORY"
    
    deactivate
else
    print_header "Step 4: Upload Preview (Dry Run)"
    print_status "Would upload the following packages:"
    ls -1 dist/
    print_status "To repository: $PYPI_REPOSITORY"
    print_status "With username: $PYPI_USERNAME"
fi

# =============================================================================
# STEP 5: Cleanup
# =============================================================================
print_header "Step 5: Cleanup"

if [ "$DRY_RUN" = false ]; then
    rm -rf .venv-publish
    print_success "Cleanup complete"
else
    print_status "DRY RUN: Would cleanup virtual environment"
fi

# =============================================================================
# Summary
# =============================================================================
print_header "Publishing Summary"

if [ "$DRY_RUN" = false ]; then
    echo -e "Publishing Complete!${NC}\n"
    echo "Package: instana-client"
    echo "Version: $CURRENT_VERSION"
    echo "Repository: $PYPI_REPOSITORY"
    echo ""
    echo "Package URL: $PACKAGE_URL"
    echo ""
    echo "Next steps:"
    echo "1. Verify package on PyPI"
    echo "2. Test installation: pip install instana-client==$CURRENT_VERSION"
    echo "3. Create git tag: git tag v$CURRENT_VERSION"
    echo "4. Push tag: git push origin v$CURRENT_VERSION"
    echo "5. Create GitHub release"
else
    echo "This was a DRY RUN - no packages were uploaded"
    echo "Run without --dry-run to publish to PyPI"
    echo ""
    echo "Packages ready for upload:"
    ls -1 dist/
fi

print_success "Publishing process complete!"

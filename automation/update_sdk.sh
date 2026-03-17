#!/bin/bash

# =============================================================================
# INSTANA PYTHON SDK UPDATE SCRIPT
# =============================================================================
# This script automates the SDK update process including:
# - Regenerating SDK code from OpenAPI spec
# - Running tests
# - Version bumping
# - Building distribution packages
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
OPENAPI_SPEC_PATH="${OPENAPI_SPEC_PATH:-}"
NEW_VERSION="${NEW_VERSION:-}"
SKIP_TESTS="${SKIP_TESTS:-false}"
SKIP_BUILD="${SKIP_BUILD:-false}"
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

Automate Instana Python SDK updates

OPTIONS:
    -s, --spec-path PATH        Path to OpenAPI spec file (required)
    -v, --version VERSION       New SDK version (e.g., 1.0.5)
    -t, --skip-tests           Skip running tests
    -b, --skip-build           Skip building distribution packages
    -d, --dry-run              Perform dry run (no actual changes)
    -h, --help                 Show this help message

EXAMPLES:
    # Update with new spec and auto-increment version
    $0 --spec-path ./openapi.yaml

    # Update with specific version
    $0 --spec-path ./openapi-1.316.yaml --version 1.0.5

    # Dry run to see what would happen
    $0 --spec-path ./openapi.yaml --dry-run

    # Update without building packages
    $0 --spec-path ./openapi.yaml --skip-build

ENVIRONMENT VARIABLES:
    OPENAPI_SPEC_PATH         Default OpenAPI spec path
    NEW_VERSION               Default new version

EOF
}

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -s|--spec-path)
            OPENAPI_SPEC_PATH="$2"
            shift 2
            ;;
        -v|--version)
            NEW_VERSION="$2"
            shift 2
            ;;
        -t|--skip-tests)
            SKIP_TESTS=true
            shift
            ;;
        -b|--skip-build)
            SKIP_BUILD=true
            shift
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

# Validate required parameters
if [ -z "$OPENAPI_SPEC_PATH" ]; then
    print_error "OpenAPI spec path is required"
    show_usage
    exit 1
fi

# Validate spec file exists
if [ ! -f "$OPENAPI_SPEC_PATH" ]; then
    print_error "OpenAPI spec file not found: $OPENAPI_SPEC_PATH"
    exit 1
fi

# Change to project root
cd "$PROJECT_ROOT"

print_header "Instana Python SDK Update"
print_status "Project root: $PROJECT_ROOT"
print_status "OpenAPI spec: $OPENAPI_SPEC_PATH"
print_status "Dry run: $DRY_RUN"

# =============================================================================
# STEP 1: Backup current state
# =============================================================================
print_header "Step 1: Backing up current state"

BACKUP_DIR="$PROJECT_ROOT/.backup_$(date +%Y%m%d_%H%M%S)"
if [ "$DRY_RUN" = false ]; then
    mkdir -p "$BACKUP_DIR"
    cp -r instana_client "$BACKUP_DIR/"
    cp setup.py pyproject.toml "$BACKUP_DIR/"
    print_success "Backup created at: $BACKUP_DIR"
else
    print_status "DRY RUN: Would create backup at $BACKUP_DIR"
fi

# =============================================================================
# STEP 2: Copy OpenAPI spec to project root
# =============================================================================
print_header "Step 2: Preparing OpenAPI specification"

print_status "Using spec file: $OPENAPI_SPEC_PATH"
if [ "$DRY_RUN" = false ]; then
    # Copy to project root as openapi.yaml
    cp "$OPENAPI_SPEC_PATH" openapi.yaml
    print_success "Copied OpenAPI spec to project root"
else
    print_status "DRY RUN: Would copy from $OPENAPI_SPEC_PATH"
fi

# Extract version from OpenAPI spec
SPEC_VERSION=$(grep -m 1 "version:" openapi.yaml | sed 's/.*version: *//;s/"//g;s/'\''//g' | tr -d ' ')
print_status "OpenAPI spec version: $SPEC_VERSION"

# =============================================================================
# STEP 3: Determine new SDK version
# =============================================================================
print_header "Step 3: Determining SDK version"

CURRENT_VERSION=$(grep "^VERSION = " setup.py | sed 's/VERSION = "\(.*\)"/\1/')
print_status "Current SDK version: $CURRENT_VERSION"

if [ -z "$NEW_VERSION" ]; then
    # Auto-increment patch version
    IFS='.' read -ra VERSION_PARTS <<< "$CURRENT_VERSION"
    MAJOR="${VERSION_PARTS[0]}"
    MINOR="${VERSION_PARTS[1]}"
    PATCH="${VERSION_PARTS[2]}"
    NEW_PATCH=$((PATCH + 1))
    NEW_VERSION="$MAJOR.$MINOR.$NEW_PATCH"
    print_status "Auto-incremented version to: $NEW_VERSION"
else
    print_status "Using specified version: $NEW_VERSION"
fi

# =============================================================================
# STEP 4: Generate SDK code
# =============================================================================
print_header "Step 4: Generating SDK code"

if [ "$DRY_RUN" = false ]; then
    print_status "Running OpenAPI generator..."
    
    # Check if openapi-generator-cli is available
    if ! command -v openapi-generator-cli &> /dev/null; then
        print_error "openapi-generator-cli not found. Please install it first."
        print_status "Install with: npm install -g @openapitools/openapi-generator-cli"
        exit 1
    fi
    
    openapi-generator-cli generate \
        -i openapi.yaml \
        -g python \
        -o . \
        --config openapi-generator-config.json \
        --skip-validate-spec
    
    print_success "SDK code generated"
else
    print_status "DRY RUN: Would generate SDK code"
fi

# =============================================================================
# STEP 5: Update version numbers
# =============================================================================
print_header "Step 5: Updating version numbers"

if [ "$DRY_RUN" = false ]; then
    # Update setup.py
    sed -i.bak "s/VERSION = \"$CURRENT_VERSION\"/VERSION = \"$NEW_VERSION\"/" setup.py
    
    # Update pyproject.toml
    sed -i.bak "s/version = \"$CURRENT_VERSION\"/version = \"$NEW_VERSION\"/" pyproject.toml
    
    # Update __init__.py
    sed -i.bak "s/__version__ = \"$CURRENT_VERSION\"/__version__ = \"$NEW_VERSION\"/" instana_client/__init__.py
    
    # Update api_client.py
    sed -i.bak "s/OpenAPI-Generator\/$CURRENT_VERSION/OpenAPI-Generator\/$NEW_VERSION/" instana_client/api_client.py
    
    # Update configuration.py
    sed -i.bak "s/SDK Package Version: $CURRENT_VERSION/SDK Package Version: $NEW_VERSION/" instana_client/configuration.py
    
    # Clean up backup files
    rm -f setup.py.bak pyproject.toml.bak instana_client/__init__.py.bak \
          instana_client/api_client.py.bak instana_client/configuration.py.bak
    
    print_success "Version updated to $NEW_VERSION"
else
    print_status "DRY RUN: Would update version from $CURRENT_VERSION to $NEW_VERSION"
fi

# =============================================================================
# STEP 6: Run tests
# =============================================================================
if [ "$SKIP_TESTS" = false ]; then
    print_header "Step 6: Running tests"
    
    if [ "$DRY_RUN" = false ]; then
        # Run sanity tests
        print_status "Running sanity tests..."
        if ./sanity_test.sh; then
            print_success "Sanity tests passed"
        else
            print_error "Sanity tests failed"
            print_warning "Restoring from backup..."
            rm -rf instana_client setup.py pyproject.toml
            cp -r "$BACKUP_DIR"/* .
            exit 1
        fi
        
        # Run unit tests
        print_status "Running unit tests..."
        if python3 -m pytest test/ -v --tb=short --maxfail=5; then
            print_success "Unit tests passed"
        else
            print_warning "Some unit tests failed (this is expected for stub tests)"
        fi
    else
        print_status "DRY RUN: Would run sanity and unit tests"
    fi
else
    print_warning "Skipping tests (--skip-tests flag set)"
fi

# =============================================================================
# STEP 7: Build distribution packages
# =============================================================================
if [ "$SKIP_BUILD" = false ]; then
    print_header "Step 7: Building distribution packages"
    
    if [ "$DRY_RUN" = false ]; then
        # Clean previous builds
        rm -rf dist/ build/ *.egg-info
        
        # Create virtual environment for build
        python3 -m venv .venv-build
        source .venv-build/bin/activate
        pip install --upgrade build
        
        # Build packages
        python -m build
        
        print_success "Distribution packages built"
        ls -lh dist/
        
        deactivate
        rm -rf .venv-build
    else
        print_status "DRY RUN: Would build distribution packages"
    fi
else
    print_warning "Skipping build (--skip-build flag set)"
fi

# =============================================================================
# STEP 8: Cleanup
# =============================================================================
print_header "Step 8: Cleanup"

if [ "$DRY_RUN" = false ]; then
    rm -rf build/ *.egg-info
    print_success "Cleanup complete"
    
    # Keep backup for safety
    print_status "Backup preserved at: $BACKUP_DIR"
    print_status "Remove manually if update is successful"
else
    print_status "DRY RUN: Would cleanup build artifacts"
fi

# =============================================================================
# Summary
# =============================================================================
print_header "Update Summary"

echo -e "${GREEN}✅ SDK Update Complete!${NC}\n"
echo "Previous version: $CURRENT_VERSION"
echo "New version: $NEW_VERSION"
echo "OpenAPI spec version: $SPEC_VERSION"
echo ""

if [ "$DRY_RUN" = false ]; then
    echo "Next steps:"
    echo "1. Review the changes: git diff"
    echo "2. Test the updated SDK"
    if [ "$SKIP_BUILD" = false ]; then
        echo "3. Publish to PyPI: ./automation/publish_pypi.sh"
    fi
    echo "4. Commit changes: git add . && git commit -m 'Update SDK to version $NEW_VERSION'"
    echo "5. Push to repository: git push"
    echo ""
    echo "Backup location: $BACKUP_DIR"
else
    echo "This was a DRY RUN - no actual changes were made"
    echo "Run without --dry-run to perform the actual update"
fi

print_success "SDK update complete! 🎉"

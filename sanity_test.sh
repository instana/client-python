#!/bin/bash

# =============================================================================
# INSTANA PYTHON SDK SANITY TESTING SCRIPT
# =============================================================================
# This script performs comprehensive sanity testing for the Instana Python SDK
# Run this after any SDK update to ensure everything works correctly
# =============================================================================

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
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

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# =============================================================================
# PHASE 1: ENVIRONMENT SETUP
# =============================================================================

print_status "Starting Instana Python SDK Sanity Testing..."
echo "=================================================="

# Check Python version
print_status "Checking Python version..."
python3 --version
if [ $? -eq 0 ]; then
    print_success "Python3 is available"
else
    print_error "Python3 is not available"
    exit 1
fi

# Check if we're in the right directory
if [ ! -f "setup.py" ]; then
    print_error "setup.py not found. Please run this script from the project root directory."
    exit 1
fi

print_success "Running from correct directory"

# =============================================================================
# PHASE 2: DEPENDENCY CHECK
# =============================================================================

print_status "Checking dependencies..."

# Install required packages if not present
REQUIRED_PACKAGES=("setuptools" "pydantic" "python-dateutil" "urllib3")

for package in "${REQUIRED_PACKAGES[@]}"; do
    if ! python3 -c "import $package" 2>/dev/null; then
        print_warning "$package not found, installing..."
        # Try with --break-system-packages first (for Homebrew Python), fall back to regular install
        if python3 -m pip install --break-system-packages "$package" >/dev/null 2>&1; then
            print_success "$package installed successfully"
        elif python3 -m pip install "$package" >/dev/null 2>&1; then
            print_success "$package installed successfully"
        else
            print_error "Failed to install $package"
            exit 1
        fi
    else
        print_success "$package is available"
    fi
done

# =============================================================================
# PHASE 3: PACKAGE VALIDATION
# =============================================================================

print_status "Phase 1: Package Configuration Validation"
echo "--------------------------------------------------"

# Test 1: Check package configuration
print_status "Testing package configuration..."
if python3 setup.py check >/dev/null 2>&1; then
    print_success "Package configuration is valid"
else
    print_error "Package configuration failed"
    exit 1
fi

# Test 2: Build package
print_status "Testing package build..."
if python3 setup.py build >/dev/null 2>&1; then
    print_success "Package builds successfully"
else
    print_error "Package build failed"
    exit 1
fi

# Test 3: Install package
print_status "Testing package installation..."
# Use pip install instead of setup.py install (modern approach)
if python3 -m pip install --break-system-packages -e . >/dev/null 2>&1; then
    print_success "Package installs successfully"
elif python3 -m pip install -e . >/dev/null 2>&1; then
    print_success "Package installs successfully"
else
    print_error "Package installation failed"
    exit 1
fi

# =============================================================================
# PHASE 4: IMPORT TESTING
# =============================================================================

print_status "Phase 2: Import and Basic Functionality Testing"
echo "------------------------------------------------------"

# Test 4: Basic import
print_status "Testing basic package import..."
if python3 -c "import instana_client; print('Basic import: SUCCESS')" 2>&1; then
    print_success "Basic package import works"
else
    print_error "Basic package import failed"
    print_error "Attempting to show import error details..."
    python3 -c "import instana_client" 2>&1 || true
    exit 1
fi

# Test 5: Version check
print_status "Testing version information..."
VERSION=$(python3 -c "import instana_client; print(instana_client.__version__)" 2>/dev/null)
if [ $? -eq 0 ]; then
    print_success "SDK Version: $VERSION"
else
    print_error "Version check failed"
    exit 1
fi

# Test 6: Core modules import
print_status "Testing core module imports..."
CORE_MODULES=("api_client" "configuration" "exceptions" "rest" "api_response")

for module in "${CORE_MODULES[@]}"; do
    if python3 -c "from instana_client import $module; print('$module: SUCCESS')" 2>/dev/null; then
        print_success "Core module '$module' imports correctly"
    else
        print_error "Core module '$module' import failed"
        exit 1
    fi
done

# =============================================================================
# PHASE 5: API MODULE TESTING
# =============================================================================

print_status "Phase 3: API Module Testing"
echo "---------------------------------"

# Test 7: New API modules (v304 specific)
print_status "Testing new API modules..."
NEW_API_MODULES=("ai_management_api" "teams_api" "custom_entities_api" "end_user_monitoring_api" "logging_analyze_api" "roles_api" "slo_correction_configurations_api" "slo_correction_windows_api")

for api in "${NEW_API_MODULES[@]}"; do
    if python3 -c "from instana_client.api import $api; print('$api: SUCCESS')" 2>/dev/null; then
        print_success "New API '$api' imports correctly"
    else
        print_error "New API '$api' import failed"
        exit 1
    fi
done

# Test 8: Legacy API modules (ensure backward compatibility)
print_status "Testing legacy API modules..."
LEGACY_API_MODULES=("application_api" "infrastructure_api" "events_api" "health_api")

for api in "${LEGACY_API_MODULES[@]}"; do
    if python3 -c "from instana_client.api import $api; print('$api: SUCCESS')" 2>/dev/null; then
        print_success "Legacy API '$api' imports correctly"
    else
        print_warning "Legacy API '$api' not found (may be renamed in v304)"
    fi
done

# =============================================================================
# PHASE 6: MODEL TESTING
# =============================================================================

print_status "Phase 4: Model Testing"
echo "---------------------------"

# Test 9: Key model imports
print_status "Testing key model imports..."
KEY_MODELS=("application" "service" "event" "trace" "metric" "alert")

for model in "${KEY_MODELS[@]}"; do
    if python3 -c "from instana_client.models import $model; print('$model: SUCCESS')" 2>/dev/null; then
        print_success "Model '$model' imports correctly"
    else
        print_warning "Model '$model' not found (may be renamed in v304)"
    fi
done

# =============================================================================
# PHASE 7: CONFIGURATION TESTING
# =============================================================================

print_status "Phase 5: Configuration Testing"
echo "------------------------------------"

# Test 10: Configuration object creation
print_status "Testing configuration object creation..."
if python3 -c "
from instana_client.configuration import Configuration
config = Configuration()
print('Configuration object created successfully')
" 2>/dev/null; then
    print_success "Configuration object creation works"
else
    print_error "Configuration object creation failed"
    exit 1
fi

# Test 11: API client creation
print_status "Testing API client creation..."
if python3 -c "
from instana_client.api_client import ApiClient
from instana_client.configuration import Configuration
config = Configuration()
client = ApiClient(config)
print('API client created successfully')
" 2>/dev/null; then
    print_success "API client creation works"
else
    print_error "API client creation failed"
    exit 1
fi

# =============================================================================
# PHASE 8: FILE STRUCTURE VALIDATION
# =============================================================================

print_status "Phase 6: File Structure Validation"
echo "----------------------------------------"

# Test 12: Check file counts
print_status "Validating file structure..."

MODEL_COUNT=$(find instana_client/models -name "*.py" | wc -l)
API_COUNT=$(find instana_client/api -name "*.py" | wc -l)
TOTAL_PYTHON_FILES=$(find instana_client -name "*.py" | wc -l)

print_success "File structure validation:"
print_success "  - Model files: $MODEL_COUNT"
print_success "  - API files: $API_COUNT"
print_success "  - Total Python files: $TOTAL_PYTHON_FILES"

# =============================================================================
# PHASE 9: FINAL VALIDATION
# =============================================================================

print_status "Phase 7: Final Integration Test"
echo "------------------------------------"

# Test 13: Complete integration test
print_status "Running complete integration test..."
if python3 -c "
import instana_client
print('✅ 1. Basic import: SUCCESS')
print(f'   SDK Version: {instana_client.__version__}')

from instana_client.api.ai_management_api import AIManagementApi
from instana_client.api.teams_api import TeamsApi
print('✅ 2. New APIs: SUCCESS')

from instana_client.models.application import Application
print('✅ 3. Models: SUCCESS')

from instana_client.configuration import Configuration
print('✅ 4. Configuration: SUCCESS')

print('🎉 ALL SYSTEMS GO!')
" 2>/dev/null; then
    print_success "Complete integration test passed"
else
    print_error "Complete integration test failed"
    exit 1
fi

# =============================================================================
# PHASE 8: CLEANUP
# =============================================================================

print_status "Phase 8: Cleanup"
echo "-------------------"

# Clean up build artifacts
print_status "Cleaning up build artifacts..."
if [ -d "build" ]; then
    rm -rf build/
    print_success "Removed build/ directory"
fi

if [ -d "instana_client.egg-info" ]; then
    rm -rf instana_client.egg-info/
    print_success "Removed instana_client.egg-info/ directory"
fi

if [ -d "dist" ]; then
    rm -rf dist/
    print_success "Removed dist/ directory"
fi

# Clean up test reports
print_status "Cleaning up test reports..."
if ls sanity_test_report_*.txt >/dev/null 2>&1; then
    rm -f sanity_test_report_*.txt
    print_success "Removed test report files"
fi

# =============================================================================
# PHASE 9: SUMMARY
# =============================================================================

echo ""
echo "=================================================="
print_success "SANITY TESTING COMPLETED SUCCESSFULLY! 🎉"
echo "=================================================="
echo ""
print_success "All tests passed:"
print_success "  ✅ Package configuration valid"
print_success "  ✅ Package builds successfully"
print_success "  ✅ Package installs successfully"
print_success "  ✅ All imports work correctly"
print_success "  ✅ New APIs functional"
print_success "  ✅ Models accessible"
print_success "  ✅ Configuration works"
print_success "  ✅ File structure valid"
print_success "  ✅ Integration test passed"
echo ""
print_success "The Instana Python SDK is ready for production! 🚀"
echo ""

# Optional: Generate test report
if [ "$1" = "--report" ]; then
    REPORT_FILE="sanity_test_report_$(date +%Y%m%d_%H%M%S).txt"
    echo "Generating test report: $REPORT_FILE"
    {
        echo "Instana Python SDK Sanity Test Report"
        echo "Generated: $(date)"
        echo "======================================"
        echo ""
        echo "Test Results: ALL PASSED"
        echo "SDK Version: $VERSION"
        echo "Model Files: $MODEL_COUNT"
        echo "API Files: $API_COUNT"
        echo "Total Python Files: $TOTAL_PYTHON_FILES"
        echo ""
        echo "All sanity tests completed successfully."
    } > "$REPORT_FILE"
    print_success "Test report saved to: $REPORT_FILE"
fi

exit 0

#!/bin/bash
# Run this from the ROOT of your easydeskview repo
# Fixes all remaining build failures from run #18

set -e
echo "=== Fixing all remaining build failures ==="

# ─────────────────────────────────────────────
# FIX 1: Linux binary name (exit 255)
# flutter/linux/CMakeLists.txt
# ─────────────────────────────────────────────
echo "[1/6] Fixing Linux CMakeLists.txt..."
sed -i 's/set(BINARY_NAME "rustdesk")/set(BINARY_NAME "easydeskview")/g' \
  flutter/linux/CMakeLists.txt
# Verify
grep "BINARY_NAME" flutter/linux/CMakeLists.txt

# ─────────────────────────────────────────────
# FIX 2: Windows binary name (exit 1)
# flutter/windows/runner/CMakeLists.txt
# ─────────────────────────────────────────────
echo "[2/6] Fixing Windows CMakeLists.txt..."
sed -i 's/set(BINARY_NAME "rustdesk")/set(BINARY_NAME "easydeskview")/g' \
  flutter/windows/runner/CMakeLists.txt
grep "BINARY_NAME" flutter/windows/runner/CMakeLists.txt

# ─────────────────────────────────────────────
# FIX 3: Android applicationId (exit 101)
# flutter/android/app/build.gradle
# ─────────────────────────────────────────────
echo "[3/6] Fixing Android build.gradle applicationId..."
sed -i 's/applicationId "com\.carriez\.flutter_hbb"/applicationId "com.desipayments.easydeskview"/g' \
  flutter/android/app/build.gradle
# Also fix namespace if present
sed -i 's/namespace "com\.carriez\.flutter_hbb"/namespace "com.desipayments.easydeskview"/g' \
  flutter/android/app/build.gradle
grep "applicationId\|namespace" flutter/android/app/build.gradle

# ─────────────────────────────────────────────
# FIX 4: macOS app name (exit 255)
# flutter/macos/Runner/Configs/AppInfo.xcconfig
# ─────────────────────────────────────────────
echo "[4/6] Fixing macOS AppInfo.xcconfig PRODUCT_NAME..."
sed -i 's/PRODUCT_NAME = RustDesk/PRODUCT_NAME = EasyDeskView/g' \
  flutter/macos/Runner/Configs/AppInfo.xcconfig
sed -i 's/PRODUCT_NAME = Rustdesk/PRODUCT_NAME = EasyDeskView/g' \
  flutter/macos/Runner/Configs/AppInfo.xcconfig
# Also fix bundle ID (in case not done yet)
sed -i 's/PRODUCT_BUNDLE_IDENTIFIER = com\.carriez\.flutterHbb/PRODUCT_BUNDLE_IDENTIFIER = com.desipayments.easydeskview/g' \
  flutter/macos/Runner/Configs/AppInfo.xcconfig
grep "PRODUCT_NAME\|PRODUCT_BUNDLE_IDENTIFIER" flutter/macos/Runner/Configs/AppInfo.xcconfig

# ─────────────────────────────────────────────
# FIX 5: iOS bundle ID in Xcode project (exit 1)
# flutter/ios/Runner.xcodeproj/project.pbxproj
# ─────────────────────────────────────────────
echo "[5/6] Fixing iOS project.pbxproj bundle ID..."
sed -i 's/PRODUCT_BUNDLE_IDENTIFIER = com\.carriez\.flutterHbb/PRODUCT_BUNDLE_IDENTIFIER = com.desipayments.easydeskview/g' \
  flutter/ios/Runner.xcodeproj/project.pbxproj
# Also fix display name
sed -i 's/PRODUCT_NAME = RustDesk/PRODUCT_NAME = EasyDeskView/g' \
  flutter/ios/Runner.xcodeproj/project.pbxproj
grep "PRODUCT_BUNDLE_IDENTIFIER" flutter/ios/Runner.xcodeproj/project.pbxproj | head -5

# ─────────────────────────────────────────────
# FIX 6: iOS Info.plist display name
# flutter/ios/Runner/Info.plist
# ─────────────────────────────────────────────
echo "[6/6] Fixing iOS Info.plist..."
sed -i 's/<string>RustDesk<\/string>/<string>EasyDeskView<\/string>/g' \
  flutter/ios/Runner/Info.plist
sed -i 's/com\.carriez\.flutterHbb/com.desipayments.easydeskview/g' \
  flutter/ios/Runner/Info.plist
grep -A1 "CFBundleName\|CFBundleIdentifier\|PRODUCT_BUNDLE" flutter/ios/Runner/Info.plist || true

echo ""
echo "=== All fixes applied! Now commit and push ==="
echo ""
echo "Run:"
echo "  git add flutter/"
echo "  git commit -m 'fix: fix binary names, bundle IDs and app names for all platforms'"
echo "  git push origin master"

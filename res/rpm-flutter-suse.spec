Name:       easydeskview
Version:    1.4.5
Release:    0
Summary:    RPM package
License:    GPL-3.0
URL:        https://easydeskview.com
Vendor:     easydeskview <support@easydeskview.com>
Requires:   gtk3 libxcb1 libXfixes3 alsa-utils libXtst6 libva2 pam gstreamer-plugins-base gstreamer-plugin-pipewire
Recommends: libayatana-appindicator3-1 xdotool
Provides:   libdesktop_drop_plugin.so()(64bit), libdesktop_multi_window_plugin.so()(64bit), libfile_selector_linux_plugin.so()(64bit), libflutter_custom_cursor_plugin.so()(64bit), libflutter_linux_gtk.so()(64bit), libscreen_retriever_plugin.so()(64bit), libtray_manager_plugin.so()(64bit), liburl_launcher_linux_plugin.so()(64bit), libwindow_manager_plugin.so()(64bit), libwindow_size_plugin.so()(64bit), libtexture_rgba_renderer_plugin.so()(64bit)

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Scriptlets/

%description
The best open-source remote desktop client software, written in Rust.

%prep
# we have no source, so nothing here

%build
# we have no source, so nothing here

# %global __python %{__python3}

%install

mkdir -p "%{buildroot}/usr/share/easydeskview" && cp -r ${HBB}/flutter/build/linux/x64/release/bundle/* -t "%{buildroot}/usr/share/easydeskview"
mkdir -p "%{buildroot}/usr/bin"
install -Dm 644 $HBB/res/easydeskview.service -t "%{buildroot}/usr/share/easydeskview/files"
install -Dm 644 $HBB/res/easydeskview.desktop -t "%{buildroot}/usr/share/easydeskview/files"
install -Dm 644 $HBB/res/easydeskview-link.desktop -t "%{buildroot}/usr/share/easydeskview/files"
install -Dm 644 $HBB/res/128x128@2x.png "%{buildroot}/usr/share/icons/hicolor/256x256/apps/easydeskview.png"
install -Dm 644 $HBB/res/scalable.svg "%{buildroot}/usr/share/icons/hicolor/scalable/apps/easydeskview.svg"
install -Dm 644 $HBB/res/128x128@2x.png "%{buildroot}/usr/share/icons/hicolor/256x256/apps/easydeskview.png"
install -Dm 644 $HBB/res/scalable.svg "%{buildroot}/usr/share/icons/hicolor/scalable/apps/easydeskview.svg"

%files
/usr/share/easydeskview/*
/usr/share/easydeskview/files/easydeskview.service
/usr/share/icons/hicolor/256x256/apps/easydeskview.png
/usr/share/icons/hicolor/scalable/apps/easydeskview.svg
/usr/share/icons/hicolor/256x256/apps/easydeskview.png
/usr/share/icons/hicolor/scalable/apps/easydeskview.svg
/usr/share/easydeskview/files/easydeskview.desktop
/usr/share/easydeskview/files/easydeskview-link.desktop

%changelog
# let's skip this for now

%pre
# can do something for centos7
case "$1" in
  1)
    # for install
  ;;
  2)
    # for upgrade
    systemctl stop easydeskview || true
  ;;
esac

%post
cp /usr/share/easydeskview/files/easydeskview.service /etc/systemd/system/easydeskview.service
cp /usr/share/easydeskview/files/easydeskview.desktop /usr/share/applications/
cp /usr/share/easydeskview/files/easydeskview-link.desktop /usr/share/applications/
if [ -f /usr/share/easydeskview/easydeskview ]; then
  ln -sf /usr/share/easydeskview/easydeskview /usr/bin/easydeskview
fi
systemctl daemon-reload
systemctl enable easydeskview
systemctl start easydeskview
update-desktop-database

%preun
case "$1" in
  0)
    # for uninstall
    systemctl stop easydeskview || true
    systemctl disable easydeskview || true
    rm /etc/systemd/system/easydeskview.service || true
  ;;
  1)
    # for upgrade
  ;;
esac

%postun
case "$1" in
  0)
    # for uninstall
    rm /usr/bin/easydeskview || true
    rmdir /usr/share/easydeskview || true
    rm /usr/share/applications/easydeskview.desktop || true
    rm /usr/share/applications/easydeskview-link.desktop || true
    update-desktop-database
  ;;
  1)
    # for upgrade
  ;;
esac

Name:       easydeskview
Version:    1.1.9
Release:    0
Summary:    RPM package
License:    GPL-3.0
Requires:   gtk3 libxcb1 libXfixes3 alsa-utils libXtst6 libva2 pam gstreamer-plugins-base gstreamer-plugin-pipewire
Recommends: libayatana-appindicator3-1 xdotool

# https://docs.fedoraproject.org/en-US/packaging-guidelines/Scriptlets/

%description
The best open-source remote desktop client software, written in Rust.

%prep
# we have no source, so nothing here

%build
# we have no source, so nothing here

%global __python %{__python3}

%install
mkdir -p %{buildroot}/usr/bin/
mkdir -p %{buildroot}/usr/share/easydeskview/
mkdir -p %{buildroot}/usr/share/easydeskview/files/
mkdir -p %{buildroot}/usr/share/icons/hicolor/256x256/apps/
mkdir -p %{buildroot}/usr/share/icons/hicolor/scalable/apps/
install -m 755 $HBB/target/release/rustdesk %{buildroot}/usr/bin/easydeskview
install $HBB/libsciter-gtk.so %{buildroot}/usr/share/easydeskview/libsciter-gtk.so
install $HBB/res/easydeskview.service %{buildroot}/usr/share/easydeskview/files/
install $HBB/res/128x128@2x.png %{buildroot}/usr/share/icons/hicolor/256x256/apps/easydeskview.png
install $HBB/res/scalable.svg %{buildroot}/usr/share/icons/hicolor/scalable/apps/easydeskview.svg
install $HBB/res/128x128@2x.png %{buildroot}/usr/share/icons/hicolor/256x256/apps/easydeskview.png
install $HBB/res/scalable.svg %{buildroot}/usr/share/icons/hicolor/scalable/apps/easydeskview.svg
install $HBB/res/easydeskview.desktop %{buildroot}/usr/share/easydeskview/files/
install $HBB/res/easydeskview-link.desktop %{buildroot}/usr/share/easydeskview/files/

%files
/usr/bin/easydeskview
/usr/share/easydeskview/libsciter-gtk.so
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
    rm /usr/share/applications/easydeskview.desktop || true
    rm /usr/share/applications/easydeskview-link.desktop || true
    update-desktop-database
  ;;
  1)
    # for upgrade
  ;;
esac

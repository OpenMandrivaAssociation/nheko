Name: nheko
Version: 0.10.0
Release: 2
Group:   Networking/Instant Messenger
License: GPLv3
Summary: Desktop client for the Matrix protocol
URL: https://github.com/Nheko-Reborn/nheko
Source0: https://github.com/Nheko-Reborn/nheko/archive/v%{version}/%{name}-%{version}.tar.gz
 
BuildRequires: a2x
BuildRequires: qmake5
BuildRequires: cmake(MatrixClient)
BuildRequires: cmake(Olm)
BuildRequires: cmake(Qt5Concurrent)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5DBus)
BuildRequires: cmake(Qt5Keychain)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires: cmake(Qt5Multimedia)
BuildRequires: cmake(Qt5Network)
BuildRequires: cmake(Qt5Qml)
BuildRequires: cmake(Qt5QuickCompiler)
BuildRequires: cmake(Qt5QuickControls2)
BuildRequires: cmake(Qt5QuickWidgets)
BuildRequires: cmake(Qt5Svg)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(mpark_variant)
BuildRequires: cmake(nlohmann_json) 
BuildRequires: cmake(spdlog) 
BuildRequires: pkgconfig(coeurl)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-app-1.0)
BuildRequires: pkgconfig(gstreamer-audio-1.0)
BuildRequires: pkgconfig(gstreamer-base-1.0)
BuildRequires: pkgconfig(gstreamer-sdp-1.0)
BuildRequires: pkgconfig(gstreamer-video-1.0)
BuildRequires: pkgconfig(gstreamer-webrtc-1.0)
BuildRequires: pkgconfig(libcmark) >= 0.29.0
BuildRequires: pkgconfig(libcrypto)
BuildRequires: pkgconfig(libevent)
BuildRequires: pkgconfig(lmdb)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-ewmh)
BuildRequires: pkgconfig(zlib)
BuildRequires: asciidoc
BuildRequires: cmake
BuildRequires: appstream-util
BuildRequires: lmdbxx-devel >= 1.0.0
 
Requires: hicolor-icon-theme
Requires: qt-jdenticon
Requires: qt5-qtquickcontrols2
Requires: qt5-qtdeclarative-animation

# Need on non Qt5 system installations as gnome, xfce or mate

Requires: qt5-qtmultimedia
Requires: qt5-qtgraphicaleffects
Requires: %{_lib}qt5core5
 
Recommends: google-noto-emoji-color-fonts
Recommends: google-noto-emoji-fonts
 
# https://github.com/Nheko-Reborn/nheko/issues/391
Provides: bundled(blurhash) = 0.0.1
Provides: bundled(cpp-httplib) = 0.5.12
Provides: bundled(qtsingleapplication-qt5) = 3.2.0-gitdc8042b
 
%description
The motivation behind the project is to provide a native desktop app
for Matrix that feels more like a mainstream chat app.
 
%prep
%autosetup -p1
 
%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON \
    -DCOMPILE_QML:BOOL=OFF \
    -DHUNTER_ENABLED:BOOL=OFF \
    -DCI_BUILD:BOOL=OFF \
    -DASAN:BOOL=OFF \
    -DQML_DEBUGGING:BOOL=OFF \
    -DBUILD_DOCS:BOOL=OFF \
    -DVOIP:BOOL=ON \
    -DMAN:BOOL=ON \
    -DUSE_BUNDLED_CMARK:BOOL=OFF \
    -DUSE_BUNDLED_COEURL:BOOL=OFF \
    -DUSE_BUNDLED_GTEST:BOOL=OFF \
    -DUSE_BUNDLED_JSON:BOOL=OFF \
    -DUSE_BUNDLED_LIBEVENT:BOOL=OFF \
    -DUSE_BUNDLED_LMDB:BOOL=OFF \
    -DUSE_BUNDLED_LMDBXX:BOOL=OFF \
    -DUSE_BUNDLED_MTXCLIENT:BOOL=OFF \
    -DUSE_BUNDLED_OLM:BOOL=OFF \
    -DUSE_BUNDLED_OPENSSL:BOOL=OFF \
    -DUSE_BUNDLED_QTKEYCHAIN:BOOL=OFF \
    -DUSE_BUNDLED_SPDLOG:BOOL=OFF
%make_build

%install
%make_install -C build

%files
%doc README.md CHANGELOG.md
%license COPYING
%{_bindir}/%{name}
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/zsh/site-functions/_nheko
%{_mandir}/man1/%{name}.1*

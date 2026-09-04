# set to nil when packaging a release,
# or the long commit tag for the specific git branch
%define commit_tag 90ff9c6f36dd9df9e0e23212c34b83ec61772bba

# when using a commit_tag (i.e. not nil) add a commit date
# decoration ~0.yyyyMMdd to Version number
%if "%{commit_tag}" != "%{nil}"
%define commit_date 20260508
%endif

Name: nheko
Version: 0.12.2%{?commit_date:~0.%{commit_date}}
Release: 3
Group:   Networking/Instant Messenger
License: GPLv3
Summary: Desktop client for the Matrix protocol
URL: https://github.com/Nheko-Reborn/nheko

# change the source URL depending on if the package is a release version or a git version
%if "%{commit_tag}" != "%{nil}"
Source0:        %url/archive/%{commit_tag}/%{name}-%{version}.tar.gz
%else
Source0:        %url/archive/%{version}/%{name}-%{version}.tar.gz
%endif

BuildSystem:   cmake
BuildOption:   -DCMAKE_BUILD_TYPE=Release
BuildOption:   -DCMAKE_SKIP_INSTALL_RPATH:BOOL=ON
BuildOption:   -DCOMPILE_QML:BOOL=OFF
BuildOption:   -DHUNTER_ENABLED:BOOL=OFF
BuildOption:   -DCI_BUILD:BOOL=OFF -DASAN:BOOL=OFF
BuildOption:   -DQML_DEBUGGING:BOOL=OFF
BuildOption:   -DBUILD_DOCS:BOOL=OFF     
BuildOption:   -DVOIP:BOOL=OFF -DMAN:BOOL=ON
BuildOption:   -DUSE_BUNDLED_CMARK:BOOL=OFF
BuildOption:   -DUSE_BUNDLED_COEURL:BOOL=OFF
BuildOption:   -DUSE_BUNDLED_GTEST:BOOL=OFF
BuildOption:   -DUSE_BUNDLED_JSON:BOOL=OFF
BuildOption:   -DUSE_BUNDLED_LIBEVENT:BOOL=OFF
BuildOption:   -DUSE_BUNDLED_LMDB:BOOL=OFF
BuildOption:   -DUSE_BUNDLED_LMDBXX:BOOL=OFF     
BuildOption:   -DUSE_BUNDLED_MTXCLIENT:BOOL=OFF
BuildOption:   -DUSE_BUNDLED_OLM:BOOL=OFF
BuildOption:   -DUSE_BUNDLED_OPENSSL:BOOL=OFF
BuildOption:   -DUSE_BUNDLED_QTKEYCHAIN:BOOL=OFF
BuildOption:   -DUSE_BUNDLED_SPDLOG:BOOL=OFF

BuildRequires: a2x
BuildRequires: cmake(MatrixClient) >= 0.10.1
BuildRequires: cmake(Olm)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Keychain)
BuildRequires: cmake(Qt6LinguistTools)
BuildRequires: cmake(Qt6Multimedia)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6QuickWidgets)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(mpark_variant)
BuildRequires: cmake(nlohmann_json) 
BuildRequires: cmake(spdlog) 
BuildRequires: cmake(KDSingleApplication-qt6)
BuildRequires: pkgconfig(coeurl) >= 0.3.0
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-app-1.0)
BuildRequires: pkgconfig(gstreamer-audio-1.0)
BuildRequires: pkgconfig(gstreamer-base-1.0)
BuildRequires: pkgconfig(gstreamer-sdp-1.0)
BuildRequires: pkgconfig(gstreamer-video-1.0)
BuildRequires: pkgconfig(libcmark) >= 0.29.0
BuildRequires: pkgconfig(libcrypto)
BuildRequires: pkgconfig(libevent)
BuildRequires: pkgconfig(lmdb)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(re2)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-ewmh)
BuildRequires: pkgconfig(zlib)
BuildRequires: asciidoc
BuildRequires: appstream-util
BuildRequires: lmdbxx-devel >= 1.0.0

Requires: hicolor-icon-theme

Recommends: google-noto-emoji-color-fonts
Recommends: google-noto-emoji-fonts

%patchlist


%description
The motivation behind the project is to provide a native desktop app
for Matrix that feels more like a mainstream chat app.


%files
%doc README.md CHANGELOG.md
%license COPYING
%{_bindir}/%{name}
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/zsh/site-functions/_nheko
%{_mandir}/man1/%{name}.1*

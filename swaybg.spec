Name:       swaybg
Version:	1.2.0
Release:	1
Summary:    Wallpaper tool for Wayland compositors

License:    MIT
URL:        https://github.com/swaywm/swaybg
Source0:	https://github.com/swaywm/swaybg/archive/v%{version}.tar.gz

BuildRequires:  meson >= 0.48.0
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.14
# Man page compilation
BuildRequires:  scdoc

%description
%{summary}.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%license LICENSE
%{_bindir}/swaybg
%{_mandir}/man1/swaybg.1*

Name:           kbdd
Version:        0.7.1
Release:        2%{?dist}
Summary:        Per window keyboard layout

# Upstream license ticket https://github.com/qnikst/kbdd/issues/48
License:        GPLv3+
URL:            https://github.com/qnikst/kbdd
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(glib-2.0)

Requires:       dbus

%description
Simple daemon and library to make per window layout using XKB
(X KeyBoard Extension).

%prep
%autosetup

%build
autoreconf -vfi
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README README.rst
%{_bindir}/%{name}
%{_datadir}/dbus-1/interfaces/%{name}-service-interface.xml
%{_mandir}/man1/%{name}.1*

%changelog
* Mon Jan 23 2017 vascom <vascom2@gmail.com> - 0.7.1-2
- Initial release
- Add Requires dbus

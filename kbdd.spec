Name:           kbdd
Version:        0.7.1
Release:        1%{?dist}
Summary:        Per window keyboard layout

License:        GPLv3+
URL:            https://github.com/qnikst/kbdd
Source0:        https://github.com/qnikst/kbdd/archive/v%{version}.tar.gz

BuildRequires:  automake
BuildRequires:  dbus-glib-devel


%description
Simple daemon and library to make per window layout using XKB
(X KeyBoard Extension).

%prep
%autosetup
aclocal
# automake --add-missing
autoreconf -if

%build
%configure
%make_build


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README README.rst
%{_bindir}/%{name}
%{_datadir}/dbus-1/interfaces/%{name}-service-interface.xml
%{_mandir}/man1/%{name}.1*


%changelog
* Mon Jan 23 2017 vascom <vascom2@gmail.com> - 0.7.1-1
- Initial release

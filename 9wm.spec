Summary:	An X window manager resembling the Plan 9 (8-1/2) interface
Summary(pl):	Zarz±dca okien emuluj±cy interfejs Plan 9 (8-1/2)
Name:		9wm
Version:	1.2
Release:	5
License:	distributable
Group:		X11/Window Managers
Source0:	http://www.plig.org/xwinman/archive/9wm/pre-%{name}-%{version}.shar.gz
# Source0-md5:	2785a33d4f42ecc19234029db03d7e00
Source1:	%{name}.desktop
Source2:	%{name}-xsession.desktop
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_wmpropsdir	/usr/share/wm-properties
%define		_xsessdir	/usr/share/xsessions

%description
9wm emulates the Plan 9 window manager 8-1/2. 9wm is designed to be
small and fast. The interface is easy to use, icon-less and
click-to-type.

%description -l pl
9wm emuluje zarz±dcê okien 8-1/2 z Plan 9. 9wm zosta³ zaprojektowany
tak, aby by³ ma³y i szybki. Interfejs jest ³atwy w u¿yciu i pozbawiony
ikon.

%prep
%setup -q -c -T
zcat %{SOURCE0} | sh

%build
xmkmf -a
%{__make} \
	CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_wmpropsdir},%{_xsessdir}}
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_mandir}/man1/

install 9wm $RPM_BUILD_ROOT%{_bindir}
install 9wm.man $RPM_BUILD_ROOT%{_mandir}/man1/9wm.1x

install %{SOURCE1} $RPM_BUILD_ROOT%{_wmpropsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_xsessdir}/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/9wm
%{_mandir}/*/*
%{_wmpropsdir}/*
%{_xsessdir}/%{name}.desktop

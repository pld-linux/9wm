Summary:	An X window manager resembling the Plan 9 (8-1/2) interface
Summary(pl):	Zarz±dca okien emuluj±cy interfejs Plan 9 (8-1/2)
Name:		9wm
Version:	1.2
Release:	3
License:	distributable
Group:		X11/Window Managers
Source0:	http://www.plig.org/xwinman/archive/9wm/pre-%{name}-%{version}.shar.gz
Source1:	%{name}.desktop
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	XFree86-devel

%define   _prefix /usr/X11R6
%define   _mandir /usr/X11R6/man
%define		_wmpropsdir	/usr/share/wm-properties

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
%{__make} CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_wmpropsdir}
%{__make} install install.man DESTDIR=$RPM_BUILD_ROOT
install %{SOURCE1} $RPM_BUILD_ROOT%{_wmpropsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/9wm
%{_mandir}/*/*
%{_wmpropsdir}/*

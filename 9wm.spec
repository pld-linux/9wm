Summary:	An X window manager resembling the Plan 9 (8-1/2) interface.
Summary(pl):	Zarz�dca okien emuluj�cy interfejs Pan 9 (8-1/2).
Name:		9wm
Version:	1.2
Release:	1
Copyright:	Distributable 
Group:		X11/Window Managers
Group(pl):	X11/Zarz�dcy Okien
Source0:	ftp://ftp.cs.su.oz.au/dhog/9wm/pre-%{name}-%{version}.shar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	XFree86-devel

%define _prefix /usr/X11R6
%define _mandir %{_prefix}/man

%description
9wm emulates the Plan 9 window manager 8-1/2. 9wm is designed to be
small and fast. The interface is easy to use, icon-less and
click-to-type.

%description -l pl
9wm emuluje zarz�dc� okien 8-1/2 z Plan 9. 9wm zosta� zaprojektowany
tak, aby by� ma�y i szybki. Interfejs jest �atwy w u�yciu i pozbawiony
ikon.

%prep
%setup -q -c -T
zcat %{SOURCE0} | sh

%build
xmkmf -a
%{__make} CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install install.man DESTDIR=$RPM_BUILD_ROOT
strip $RPM_BUILD_ROOT%{_bindir}/9wm

gzip -9nf README $RPM_BUILD_ROOT/%{_mandir}/man1/*

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) %{_bindir}/9wm
%{_mandir}/*/*

Summary:	An X window manager resembling the Plan 9 (8-1/2) interface
Summary(pl):	Zarz±dca okien emuluj±cy interfejs Pan 9 (8-1/2)
Name:		9wm
Version:	1.2
Release:	2
License:	distributable 
Group:		X11/Window Managers
Group(de):	X11/Fenstermanager
Group(es):	X11/Administraadores De Ventanas
Group(fr):	X11/Gestionnaires De Fenêtres
Group(pl):	X11/Zarz±dcy Okien
Source0:	ftp://ftp.cs.su.oz.au/dhog/9wm/pre-%{name}-%{version}.shar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	XFree86-devel

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

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
%{__make} install install.man DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/9wm
%{_mandir}/*/*

Summary:	GGZ Gaming Zone documentation
Summary(pl.UTF-8):	Dokumentacja platformy GGZ Gaming Zone
Name:		ggz-docs
Version:	0.0.14.1
Release:	1
License:	GPL v2+
Group:		Documentation
Source0:	http://mirrors.dotsrc.org/ggzgamingzone/ggz/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	c139158f079bf801c93eddd06d66db95
Patch0:		%{name}-info.patch
URL:		http://www.ggzgamingzone.org/
BuildRequires:	docbook-dtd31-sgml
BuildRequires:	docbook-style-dsssl
BuildRequires:	docbook-utils
BuildRequires:	ghostscript
BuildRequires:	jade
BuildRequires:	lynx
BuildRequires:	texinfo
BuildRequires:	texlive-dvips
BuildRequires:	transfig
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains reference documentation, tutorials and help for
game module writers. The client/server specification and a general
overview are also included, as well as game comparison tables and the
guides for hosting and game development.

%description -l pl.UTF-8
Ten pakiet zawiera dokumentację, przewodniki i opisy dla autorów
modułów gier. Dołączona jest także specyfikacja klienta/serwera oraz
ogólny przegląd, a także tablice porównawcze gier oraz przewodniki
dotyczące hostowania i rozwijania gier.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--enable-guides \
	--enable-spec

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS QuickStart.GGZ README README.GGZ TODO
%{_docdir}/ggz-docs
%{_infodir}/ggz-game-development-guide.info*
%{_infodir}/ggz-hosting-guide.info*

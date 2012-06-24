Summary:	Generic Hash Table library
Summary(pl):	Biblioteka - og�lna tablica mieszaj�ca
Name:		libghthash
Version:	0.5.6
Release:	0.9
License:	GPL v2
Group:		Applications
Source0:	http://www.ipd.bth.se/ska/sim_home/filer/%{name}-%{version}.tar.gz
# Source0-md5:	d7619ad6a50185dae78e018237e8150a
URL:		http://www.ipd.bth.se/ska/sim_home/libghthash.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libghthash is a Generic Hash Table which is meant to be easy to
extend, portable, clear in its code and easy to use.

%description -l pl
libghthash to og�lna tablica mieszaj�ca maj�ca by� �atwa w
rozszerzaniu, przeno�na, �atwa w u�yciu i mie� przejrzysty kod.

%package devel
Summary:	Header files for libghthash library
Summary(pl):	Pliki nag��wkowe biblioteki libghthash
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This is the package containing the header files for libghthash
library.

%description devel -l pl
Ten pakiet zawiera pliki nag��wkowe biblioteki libghthash.

%package static
Summary:	Static libghthash library
Summary(pl):	Statyczna biblioteka libghthash
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libghthash library.

%description static -l pl
Statyczna biblioteka libghthash.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc html/*
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

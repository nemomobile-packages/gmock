Name:       gmock
Version:    1.7.0
Release:    1
License:    BSD-3-Clause
Summary:    Google C++ Mocking Framework
Url:        http://code.google.com/p/googlemock/
Group:      System/Libraries
Source:     gmock-%{version}.tar.bz2

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

BuildRoot:  %{_tmppath}/%{name}-%{version}-build

%description
Inspired by jMock, EasyMock, and Hamcrest, and designed with C++'s specifics
in mind, Google C++ Mocking Framework (or Google Mock for short) is a library
for writing and using C++ mock classes.

%package -n libgmock0
Summary:    Google C++ mocking framework - Shared Libraries
Group:      System/Libraries

%description -n libgmock0
Inspired by jMock, EasyMock, and Hamcrest, and designed with C++'s specifics
in mind, Google C++ Mocking Framework (or Google Mock for short) is a library
for writing and using C++ mock classes.

%package -n libgmock-devel
Summary:    Google C++ mocking framework - Development Files
Group:      Development/Libraries/C and C++

Requires:   libgmock0 = %{version}-%{release}

%description -n libgmock-devel
Inspired by jMock, EasyMock, and Hamcrest, and designed with C++'s specifics
in mind, Google C++ Mocking Framework (or Google Mock for short) is a library
for writing and using C++ mock classes.

%prep
%setup -q -n %{name}-%{version}/%{name}

autoreconf -vfi

%build
%configure
make %{_smp_mflags}

%install
mkdir -p $RPM_BUILD_ROOT/%{_libdir}
libtool --mode install cp lib/libgmock.la $RPM_BUILD_ROOT/%{_libdir}
libtool --mode install cp lib/libgmock_main.la $RPM_BUILD_ROOT/%{_libdir}
rm $RPM_BUILD_ROOT/%{_libdir}/libgmock*.la

mkdir -p $RPM_BUILD_ROOT/%{_includedir}/gmock
cp -aR include/gmock $RPM_BUILD_ROOT/%{_includedir}

%post -n libgmock0 -p /sbin/ldconfig

%postun -n libgmock0 -p /sbin/ldconfig

%files -n libgmock0
%defattr(-,root,root)
%{_libdir}/libgmock*.so.0*

%files -n libgmock-devel
%defattr(-,root,root,0755)
%{_libdir}/libgmock*.so
%{_libdir}/libgmock*.a
%{_includedir}/gmock/

Summary:	GCC-XML - dump XML description of C++ source code
Summary(pl.UTF-8):	GCC-XML - zrzut opisu XML kodu źródłowego w C++
Name:		gccxml
Version:	0.9.0
%define	gitref	3afa8ba5be6866e603dcabe80aff79856b558e24
%define	snap	20150424
%define	rel	2
Release:	0.%{snap}.%{rel}
License:	GPL v2+ (GCC code), BSD-like (GCC-XML)
Group:		Development/Tools
Source0:	https://github.com/gccxml/gccxml/archive/%{gitref}/%{name}-%{snap}.tar.gz
# Source0-md5:	70e4b145feb2a7036c835cf214cae26a
Patch0:		%{name}-gcc.patch
URL:		http://gccxml.github.io/HTML/Index.html
BuildRequires:	cmake
BuildRequires:	libstdc++-devel
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GCC-XML program dumps an XML description of C++ source code using an
extension on the GCC C++ compiler.

%description -l pl.UTF-8
GCC-XML to program zrzucający opis XML kodu źródłowego w C++ przy
użyciu rozszerzenia kompulatora C++ GCC.

%prep
%setup -q -n %{name}-%{gitref}
%patch0 -p1

%build
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/gccxml-0.9

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.rst README.rst GCC_XML/Copyright.txt build/GCC_XML/doc/gccxml.html
%attr(755,root,root) %{_bindir}/gccxml
%attr(755,root,root) %{_bindir}/gccxml_cc1plus
%dir %{_datadir}/gccxml-0.9
%{_datadir}/gccxml-0.9/gccxml_config
%{_datadir}/gccxml-0.9/gccxml_identify_compiler.cc
%dir %{_datadir}/gccxml-0.9/GCC
%{_datadir}/gccxml-0.9/GCC/2.95
%{_datadir}/gccxml-0.9/GCC/2.96
%{_datadir}/gccxml-0.9/GCC/3.0
%{_datadir}/gccxml-0.9/GCC/3.1
%{_datadir}/gccxml-0.9/GCC/3.2
%{_datadir}/gccxml-0.9/GCC/3.3
%{_datadir}/gccxml-0.9/GCC/3.4
%{_datadir}/gccxml-0.9/GCC/4.0
%{_datadir}/gccxml-0.9/GCC/4.1
%{_datadir}/gccxml-0.9/GCC/4.2
%{_datadir}/gccxml-0.9/GCC/4.3
%{_datadir}/gccxml-0.9/GCC/4.4
%{_datadir}/gccxml-0.9/GCC/4.5
%{_datadir}/gccxml-0.9/GCC/4.6
%{_datadir}/gccxml-0.9/GCC/4.7
%{_datadir}/gccxml-0.9/GCC/4.8
%{_datadir}/gccxml-0.9/GCC/4.9
%dir %{_datadir}/gccxml-0.9/IBM
%{_datadir}/gccxml-0.9/IBM/8.0
%attr(755,root,root) %{_datadir}/gccxml-0.9/IBM/find_flags
%{_datadir}/gccxml-0.9/IBM/find_flags_common
%dir %{_datadir}/gccxml-0.9/Intel
%attr(755,root,root) %{_datadir}/gccxml-0.9/Intel/find_flags
%{_datadir}/gccxml-0.9/Intel/pthread.h
%dir %{_datadir}/gccxml-0.9/MIPSpro
%{_datadir}/gccxml-0.9/MIPSpro/7.3
%attr(755,root,root) %{_datadir}/gccxml-0.9/MIPSpro/find_flags
%{_datadir}/gccxml-0.9/MIPSpro/mipspro_defs.cxx
%dir %{_datadir}/gccxml-0.9/Sun
%{_datadir}/gccxml-0.9/Sun/5.8
%attr(755,root,root) %{_datadir}/gccxml-0.9/Sun/find_flags
%{_datadir}/gccxml-0.9/Sun/find_flags_common
%{_mandir}/man1/gccxml.1*

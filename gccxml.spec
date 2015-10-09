Summary:	GCC-XML - dump XML description of C++ source code
Summary(pl.UTF-8):	GCC-XML - zrzut opisu XML kodu źródłowego w C++
Name:		gccxml
Version:	0.6.0
Release:	1
License:	GPL v2+ (GCC code), BSD-like (GCC-XML)
Group:		Development/Tools
Source0:	https://github.com/gccxml/gccxml/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	0458765b917dc385d91e0f14156572a8
Patch0:		%{name}-includes.patch
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
%setup -q
%patch0 -p1

# replace with new version
cp -f /usr/include/obstack.h GCC/include/obstack.h

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
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/gccxml-0.6

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README GCC_XML/Copyright.txt build/bin/doc/gccxml.html
%attr(755,root,root) %{_bindir}/gccxml
%attr(755,root,root) %{_bindir}/gccxml_cc1plus
%dir %{_datadir}/gccxml-0.6
%{_datadir}/gccxml-0.6/gccxml_config
%attr(755,root,root) %{_datadir}/gccxml-0.6/gccxml_find_flags
%dir %{_datadir}/gccxml-0.6/GCC
%{_datadir}/gccxml-0.6/GCC/2.95
%{_datadir}/gccxml-0.6/GCC/3.3
%attr(755,root,root) %{_datadir}/gccxml-0.6/GCC/find_flags
%dir %{_datadir}/gccxml-0.6/Intel
%attr(755,root,root) %{_datadir}/gccxml-0.6/Intel/find_flags
%dir %{_datadir}/gccxml-0.6/MIPSpro
%{_datadir}/gccxml-0.6/MIPSpro/7.3
%attr(755,root,root) %{_datadir}/gccxml-0.6/MIPSpro/find_flags
%{_mandir}/man1/gccxml.1*

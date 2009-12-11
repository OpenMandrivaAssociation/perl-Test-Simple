%define upstream_name    Test-Simple
%define upstream_version 0.94

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary: 	Basic utilities for writing tests
License: 	GPL+ or Artistic
Group: 		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch: 	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}

%description 
This is an extremely simple, extremely basic module for writing tests suitable
for CPAN modules and other pursuits. If you wish to do more complicated
testing, use the Test::More module (a drop-in replacement for this one).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Test
%{_mandir}/*/*

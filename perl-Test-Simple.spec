%define module  Test-Simple
%define name    perl-%{module}
%define version 0.86
%define release %mkrel 1

Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Summary: 	Basic utilities for writing tests
License: 	GPL or Artistic
Group: 		Development/Perl
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Test/%{module}-%{version}.tar.gz
BuildArch: 	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}

%description 
This is an extremely simple, extremely basic module for writing tests suitable
for CPAN modules and other pursuits. If you wish to do more complicated
testing, use the Test::More module (a drop-in replacement for this one).

%prep
%setup -q -n %{module}-%{version}

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

%define modname	Test-Simple
#%%define modver 1.001009
%define modver 1.302171

Summary:	Basic utilities for writing tests


Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Test/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description 
This is an extremely simple, extremely basic module for writing tests suitable
for CPAN modules and other pursuits. If you wish to do more complicated
testing, use the Test::More module (a drop-in replacement for this one).

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
make

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Test
%{perl_vendorlib}/Test2
%{perl_vendorlib}/*.pm

%{_mandir}/man3/*

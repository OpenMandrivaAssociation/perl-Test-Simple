%define upstream_name    Test-Simple
%define upstream_version 0.98

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	8

Summary:	Basic utilities for writing tests
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz
Patch0:		Test-Simple-0.98-perl5142.diff
BuildRequires:	perl-devel
BuildArch:	noarch

%description 
This is an extremely simple, extremely basic module for writing tests suitable
for CPAN modules and other pursuits. If you wish to do more complicated
testing, use the Test::More module (a drop-in replacement for this one).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0 -p0

%build
%__perl Makefile.PL INSTALLDIRS=vendor
make

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Test
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.980.0-6mdv2012.0
+ Revision: 765749
- rebuilt for perl-5.14.2

* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.980.0-5
+ Revision: 764933
- also add the patch
- P0: added perl 5.14.2 in there, maybe helps a bit...
- and another rebuild, it needs perl-Test-Deep-0.108.0-4

* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.980.0-4
+ Revision: 764923
- rebuild

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.980.0-3
+ Revision: 764254
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.980.0-2
+ Revision: 667381
- mass rebuild

* Thu Mar 10 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.980.0-1
+ Revision: 643496
- update to new version 0.98

* Sun Feb 20 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.960.0-3
+ Revision: 639016
- rebuild to make sure it override the version shipped in core

* Sat Nov 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.960.0-2mdv2011.0
+ Revision: 597201
- rebuild

* Fri Aug 13 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.960.0-1mdv2011.0
+ Revision: 569462
- new version

* Fri Dec 11 2009 Jérôme Quelin <jquelin@mandriva.org> 0.940.0-2mdv2011.0
+ Revision: 476401
- rebuild

* Thu Sep 03 2009 Jérôme Quelin <jquelin@mandriva.org> 0.940.0-1mdv2010.0
+ Revision: 427479
- update to 0.94

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.920.0-1mdv2010.0
+ Revision: 405594
- rebuild using %%perl_convert_version

* Mon Jul 06 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.92-1mdv2010.0
+ Revision: 393002
- update to new version 0.92

* Fri Jul 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.90-1mdv2010.0
+ Revision: 391953
- update to new version 0.90

* Sun Jun 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.88-1mdv2010.0
+ Revision: 383544
- update to new version 0.88

* Wed Nov 12 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.86-1mdv2009.1
+ Revision: 302438
- update to new version 0.86

* Mon Oct 20 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.84-1mdv2009.1
+ Revision: 295517
- update to new version 0.84

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.80-2mdv2009.0
+ Revision: 268738
- rebuild early 2009.0 package (before pixel changes)

* Wed Apr 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.80-1mdv2009.0
+ Revision: 194950
- update to new version 0.80

* Thu Feb 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.78-1mdv2008.1
+ Revision: 175987
- update to new version 0.78

* Mon Feb 25 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.75-1mdv2008.1
+ Revision: 174665
- update to new version 0.75

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Nov 30 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.74-1mdv2008.1
+ Revision: 114015
- update to new version 0.74

* Fri Oct 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.72-1mdv2008.1
+ Revision: 97568
- update to new version 0.72

* Mon Sep 03 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.70-1mdv2008.0
+ Revision: 78456
- package reintroduction

  + Funda Wang <fwang@mandriva.org>
    - Created package structure for perl-Test-Simple.


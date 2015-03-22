#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Eval
%define		pnam	Closure
%include	/usr/lib/rpm/macros.perl
Summary:	Eval::Closure - safely and cleanly create closures via string eval
Summary(pl.UTF-8):	Eval::Closure - bezpieczne i czyste tworzenie dopełnień poprzez eval łańcucha
Name:		perl-Eval-Closure
Version:	0.08
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/D/DO/DOY/Eval-Closure-%{version}.tar.gz
# Source0-md5:	c2af8abc363fc9a039731be9ecf2985c
URL:		http://search.cpan.org/dist/Eval-Closure/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.30
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Sub-Exporter
BuildRequires:	perl-Try-Tiny
BuildRequires:	perl-Test-Fatal
BuildRequires:	perl-Test-Requires
BuildRequires:	perl-Test-Simple >= 0.88
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
String eval is often used for dynamic code generation. For instance,
Moose uses it heavily, to generate inlined versions of accessors and
constructors, which speeds code up at runtime by a significant amount.
String eval is not without its issues however - it's difficult to
control the scope it's used in (which determines which variables are
in scope inside the eval), and it's easy to miss compilation errors,
since eval catches them and sticks them in $@ instead.

This module attempts to solve these problems. It provides an
eval_closure function, which evals a string in a clean environment,
other than a fixed list of specified variables. Compilation errors are
rethrown automatically.

%description -l pl.UTF-8
Instrukcja eval na łańcuchu często służy do dynamicznego generowania
kodu. Np. Moose wykorzystuje ją intensywnie do generowania
wewnętrznych wersji akcesorów i konstruktorów, co znacząco przyspiesza
kod w trakcie działania. Użycie eval na łańcuchu nie jest jednak
pozbawione wad - jest trudno kontrolować zakres, w jakim jest użyte
(co określa, które zmienne są w tym zakresie) i łatwo przeoczyć błędy
kompilacji, jako że eval przechwytuje je i umieszcza w $@.

Niniejszy moduł próbuje rozwiązać te problemy. Dostarcza funkcję
eval_closure, która wylicza łańcuch w czystym środowisku, innym niż
stała lista określonych zmiennych. Błędy kompilacji są automatyczne
wyrzucane ponownie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Eval/Closure.pm
%{_mandir}/man3/Eval::Closure.3pm*

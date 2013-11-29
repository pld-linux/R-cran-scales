%define		fversion	%(echo %{version} |tr r -)
%define		modulename	scales
Summary:	Scale functions for graphics
Name:		R-cran-%{modulename}
Version:	0.2.3
Release:	1
License:	GPL v2
Group:		Applications/Math
Source0:	ftp://stat.ethz.ch/R-CRAN/src/contrib/%{modulename}_%{fversion}.tar.gz
# Source0-md5:	426e5a785d4bc5b9ba8aa10d2bc043a3
URL:		http://cran.fhcrc.org/web/packages/scales/index.html
BuildRequires:	R >= 2.8.1
BuildRequires:	R-cran-RColorBrewer
BuildRequires:	R-cran-stringr
BuildRequires:	R-cran-dichromat
BuildRequires:	R-cran-munsell >= 0.2
BuildRequires:	R-cran-plyr >= 1.2
BuildRequires:	R-cran-labeling
Requires(post,postun):	R >= 2.8.1
Requires(post,postun):	perl-base
Requires(post,postun):	textutils
Requires:	R
Requires:	R-cran-RColorBrewer
Requires:	R-cran-#, stringr
Requires:	R-cran-dichromat
Requires:	R-cran-munsell >= 0.2
Requires:	R-cran-plyr >= 1.2
Requires:	R-cran-labeling
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Scales map data to aesthetics, and provide methods for automatically
determining breaks and labels for axes and legends.

%prep
%setup -q -c

%build
R CMD build %{modulename}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library/
R CMD INSTALL %{modulename} --library=$RPM_BUILD_ROOT%{_libdir}/R/library/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{modulename}/DESCRIPTION
%{_libdir}/R/library/%{modulename}

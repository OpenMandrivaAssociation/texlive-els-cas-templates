Name:		texlive-els-cas-templates
Version:	71189
Release:	1
Summary:	Elsevier updated LaTeX templates
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/els-cas-templates
License:	lppl1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/els-cas-templates.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/els-cas-templates.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This bundle provides two class and corresponding template files
for typesetting journal articles supposed to go through
Elsevier's updated workflow. One of the sets is meant for
one-column, the other for two-column layout. These are now
accepted for submitting articles both in Elsevier's electronic
submission system and elsewhere.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/els-cas-templates
%{_texmfdistdir}/bibtex/bst/els-cas-templates
%doc %{_texmfdistdir}/doc/latex/els-cas-templates

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

%global tl_name els-cas-templates
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.4
Release:	%{tl_revision}.1
Summary:	Elsevier updated LaTeX templates
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/els-cas-templates
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/els-cas-templates.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/els-cas-templates.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This bundle provides two class and corresponding template files for
typesetting journal articles supposed to go through Elsevier's updated
workflow. One of the sets is meant for one-column, the other for two-
column layout. These are now accepted for submitting articles both in
Elsevier's electronic submission system and elsewhere.


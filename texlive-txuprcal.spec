%global tl_name txuprcal
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.00
Release:	%{tl_revision}.1
Summary:	Upright calligraphic font based on TX calligraphic
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/txuprcal
License:	gpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/txuprcal.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/txuprcal.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This small package provides a means of loading as \mathcal upright
versions of the calligraphic fonts from the TX font package. A scaled
option to provided to allow arbitrary scaling.


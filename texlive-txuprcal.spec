%global tl_name txuprcal
%global tl_revision 77682
%global tl_version 1.00

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Upright calligraphic font based on TX calligraphic
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/txuprcal
License:	gpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/txuprcal.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/txuprcal.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
This small package provides a means of loading as \mathcal upright
versions of the calligraphic fonts from the TX font package. A scaled
option to provided to allow arbitrary scaling.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from txuprcal:
Map TXUprCal.map
TL_DROPIN_EOF

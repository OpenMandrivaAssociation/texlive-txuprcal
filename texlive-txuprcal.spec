Name:		texlive-txuprcal
Version:	43327
Release:	1
Summary:	Upright calligraphic font based on TX calligraphic
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/txuprcal
License:	gpl3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/txuprcal.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/txuprcal.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This small package provides a means of loading as \mathcal an
uprighted version of the calligraphic fonts from the TX font
package. A scaled option to provided to allow arbitrary
scaling.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/txuprcal
%{_texmfdistdir}/fonts/type1/public/txuprcal
%{_texmfdistdir}/fonts/tfm/public/txuprcal
%{_texmfdistdir}/fonts/map/dvips/txuprcal
%doc %{_texmfdistdir}/doc/fonts/txuprcal

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

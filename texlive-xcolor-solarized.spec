Name:		texlive-xcolor-solarized
Version:	61719
Release:	1
Summary:	Defines the 16 colors from Ethan Schoonover's Solarized palette
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/xcolor-solarized
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xcolor-solarized.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xcolor-solarized.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xcolor-solarized.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Built on top of the xcolor package, this package defines the
sixteen colors of Ethan Schoonover's popular color palette,
Solarized, for use in documents typeset with LaTeX and Friends.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/xcolor-solarized
%{_texmfdistdir}/tex/latex/xcolor-solarized
%doc %{_texmfdistdir}/doc/latex/xcolor-solarized

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post

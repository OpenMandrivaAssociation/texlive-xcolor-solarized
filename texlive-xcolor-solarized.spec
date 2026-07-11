%global tl_name xcolor-solarized
%global tl_revision 61719

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.4
Release:	%{tl_revision}.1
Summary:	Defines the 16 colors from Ethan Schoonovers Solarized palette
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/xcolor-solarized
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xcolor-solarized.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xcolor-solarized.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xcolor-solarized.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Built on top of the xcolor package, this package defines the sixteen
colors of Ethan Schoonover's popular color palette, Solarized, for use
in documents typeset with LaTeX and Friends.


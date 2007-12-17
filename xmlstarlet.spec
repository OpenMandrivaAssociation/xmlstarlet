%define name	xmlstarlet
%define version 1.0.1
%define release %mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Command Line XML Toolkit
License:	MIT
Group:		File tools
Source:		http://xmlstar.sourceforge.net/downloads/%{name}-%{version}.tar.bz2
URL:		http://xmlstar.sourceforge.net
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-devel

%description
Command Line XML Toolkit to query/edit/transform/check XML documents

%prep
%setup -q

%build
autoheader
%configure 
%make CFLAGS="$CFLAGS" LDFLAGS="-lgcrypt"

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog NEWS README Copyright TODO
%{_bindir}/xml
%{_mandir}/man1/%{name}.1*


Summary:	A program to save streaming video to your computer
Name:		streamcapture
Version:	0.0.6
Release:	1
License:	GPL v2+
Group:		X11/Applications/Multimedia
Source0:	http://bin.ceicer.com/streamcapture/current/source/%{name}-linux-%{version}-source.tar.gz
# Source0-md5:	1993189cc7acaf06765bbc639b5c60b4
URL:		http://ceicer.org/streamcapture/index_eng.php
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	qt4-qmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A program to save streaming video to your computer.

%prep
%setup -q -n %{name}-linux-%{version}-source

%build
qmake-qt4
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p streamcapture-%{version} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/streamcapture

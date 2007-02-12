%define 	module	TwistedWeb2

Summary:	Web library for Twisted
Summary(pl.UTF-8):	Biblioteka Web dla Twisted
Name:		python-%{module}
Version:	0.2.0
Release:	0.1
License:	MIT
Group:		Libraries/Python
Source0:	http://tmrc.mit.edu/mirror/twisted/Web2/%{module}-%{version}.tar.bz2
# Source0-md5:	7d6dea006d7f1e004df9f6aad730fbee
URL:		http://twistedmatrix.com/projects/web2/
BuildRequires:	ZopeInterface
BuildRequires:	python-TwistedCore >= 2.4.0
BuildRequires:	python-devel >= 2.2
Requires:	python-TwistedCore >= 2.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Twisted Web2 is a web application server written in pure Python, with
APIs at multiple levels of abstraction to facilitate different kinds
of web programming.

%description -l pl.UTF-8
Twisted Web2 to serwer aplikacji WWW napisany w czystym Pythonie z API
o wielu poziomach abstrakcji, mających ułatwić różne rodzaje
programowania WWW.

%package doc
Summary:	Documentation for TwistedWeb2
Summary(pl.UTF-8):	Dokumentacja do TwistedWeb2
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description doc
Offline documentation for TwistedWeb2.

%description doc -l pl.UTF-8
Dokumentacja offline do TwistedWeb2.

%package examples
Summary:	Example programs for TwistedWeb2
Summary(pl.UTF-8):	Programy przykładowe do TwistedWeb2
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description examples
This package contains example programs for TwistedWeb2.

%description examples -l pl.UTF-8
Ten pakiet zawiera przykładowe programy dla TwistedWeb2.

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{rpmcflags}"
export CFLAGS
python setup.py build_ext

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man1,%{_examplesdir}/%{name}-%{version}}

python setup.py install \
	--install-purelib=%{py_sitedir} \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

cp -a doc/examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README
%{py_sitedir}/twisted/web2
%{py_sitedir}/twisted/plugins/twisted_web2.py[co]

#%files doc
#%defattr(644,root,root,755)

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}

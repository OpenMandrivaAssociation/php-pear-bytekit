%define  upstream_name bytekit
%define __noautoreq /usr/bin/php

Summary:	A command-line tool built on the PHP Bytekit extension


Name:		php-pear-%{upstream_name}
Version:	1.1.2
Release:	4
License:	BSD
Group:		Development/PHP
URL:		https://www.phpunit.de/
Source0:	http://pear.phpunit.de/get/bytekit-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-cli >= 3:5.2.1
Requires:	php-pear >= 1:1.9.4
Requires:	php-channel-phpunit
BuildArch:	noarch
BuildRequires:	php-pear
BuildRequires:	php-channel-phpunit
Suggests:	php-pear-PHPUnit >= 3.6.3
Suggests:	php-pear-File_Iterator >= 1.3.0

%description
PHPUnit is a regression testing framework used by the developer who implements
unit tests in PHP.

This package provides A command-line tool built on the PHP Bytekit
extension for PHPUnit.

%prep

%setup -q -c 
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%build

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%{_bindir}/bytekit
%{_datadir}/pear/Bytekit
%{_datadir}/pear/packages/bytekit.xml




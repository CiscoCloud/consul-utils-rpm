Name:		consul-utils
Version:	0.3.1
Release:	1%{?dist}
Summary:	Command line tools for Consul

%global consul_cli_version 0.3.1

Group:		Applications/System
License:	ASL 2.0
Source0:	https://github.com/CiscoCloud/consul-cli/releases/download/v%{consul_cli_version}/consul-cli_%{consul_cli_version}_linux_amd64.tar.gz

%description
Command line tools for Consul

%prep
%setup -T -b 0 -n consul-cli_%{consulacl_version}_linux_amd64

%install
mkdir -p %{buildroot}/%{_bindir}
cd ../consul-cli_%{consul_cli_version}_linux_amd64
cp consul-cli %{buildroot}/%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%attr(755, root, root) %{_bindir}/consul-cli

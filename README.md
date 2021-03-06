# poweredge-bios-cli

A Python CLI application for obtaining BIOS settings/attributes from Dell PowerEdge servers using the Redfish API.

## Project Status: WIP

It's very early days

Everything is subject to change. Nothing is guaranteed to work.

## Requirements
1. Python >= 3.6
2. A Dell PowerEdge server running a supported iDRAC version
3. The Redfish API enabled on said iDRAC
4. The credentials for an account on said iDRAC with at least "read-only" permissions

## How to install

1. `git clone https://github.com/bcrisp4/poweredge-bios-cli.git`
2. `cd poweredge-bios-cli`
3. `pip install .`

...(probably)

## How to use

`poweredge-bios-cli -h <idrac_hostname> -u <idrac_username> -p <idrac_password> get <bios_attribute|all>`

Don't want to have the password in the command? Very sensible. Just omit the -p option and you'll be promted to enter it interactively (also works for host/-h and user/-u).

Full usage:
```
Usage: poweredge-bios-cli [OPTIONS] COMMAND [ARGS]...

  A command-line interface for the Dell PowerEdge server BIOS using the
  RedFish API.

  NOTE: RedFish must be enabled on the server iDRAC for this to work and the
  user you specify must have the relevant permissions granted to interact
  with the BIOS via the API.

  The options --host, --username and --password are required. If these
  options are not specified, you will be prompted to provide values for
  these options interactively.

  For more information on the Dell implementation of RedFish on PowerEdge
  servers, see https://dell.to/30gB3Fu

Options:
  -h, --host TEXT       The hostname or IP of the server iDRAC interface.
                        [required]
  -u, --username TEXT   The iDRAC username to use for authentication.
                        [required]
  -p, --password TEXT   The password for the specified iDRAC user.  [required]
  --verify-ssl BOOLEAN  Verify SSL/TLS certificates. Defaults to 'true'.
  --help                Show this message and exit.

Commands:
  get  Get the specified attributes or all attributes if 'all' is specified.
```

## Links

- https://www.dmtf.org/standards/redfish
- https://www.dell.com/support/manuals/uk/en/ukbsdt1/idrac7-8-lifecycle-controller-v2.40.40.40/redfish%202.40.40.40/overview?guid=guid-e85fd9c0-f4d1-4eff-be5d-550ebb77ff0d&lang=en-us




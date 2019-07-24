# IPStack for Python (Geo Location Library)
> **IPStack for Python** is a simple library used to interface with an IPStack Geo API.
>
> **Hint**: IPStack for PHP is available through `Python PIP`. `pip install ipstack`


#### Supports Python 2.7+

[![PyPI version](https://badge.fury.io/py/ipstack.svg)](https://badge.fury.io/py/ipstack)
[![PyCodeStyle](./stylebadge.svg)](./tests/latest.stylelog)
[![Downloads](https://pepy.tech/badge/ipstack)](https://pepy.tech/project/ipstack)
[![GitHub issues](https://img.shields.io/github/issues/nathan-fiscaletti/ipstackgeo-py.svg)](https://github.com/nathan-fiscaletti/ipstackgeo-py/issues)
[![GitHub license](https://img.shields.io/github/license/nathan-fiscaletti/ipstackgeo-py.svg)](https://github.com/nathan-fiscaletti/ipstackgeo-py/blob/master/LICENSE)

Learn more about IPStack here: [ipstack.net](https://ipstack.com/product)

[Looking for the PHP version?](https://github.com/nathan-fiscaletti/ipstackgeo-php)

### Features
* Retrieve the Geo Location data for any IP address.
* Retrieve the Geo Location data for the system executing this code.
* Retrieve the Geo Location data for a client.
* Retrieve the Geo Location data for a batch of IP addresses.
* Assess the security of an IP address.

---

### Basic Usage

```python
from ipstack import GeoLookup
geo_lookup = GeoLookup(".....")
location = geo_lookup.get_location("github.com")
print(location)
```

### Example Usage

> Note: See [IPStack: Response Objects](https://ipstack.com/documentation#objects) for a list of available properties in a response object.

#### Create the GeoLookup object

```python
from ipstack import GeoLookup

# Create the GeoLookup object using your API key.
geo_lookup = GeoLookup("acecac3893c90871c3")
```

#### Lookup a location for an IP Address

```python
# Lookup a location for an IP Address
# and catch any exceptions that might
# be thrown
try:
    # Retrieve the location information for 
    # github.com by using it's hostname.
    # 
    # This function will work with hostnames
    # or IP addresses.
    location = geo_lookup.get_location("github.com")
    
    # If we are unable to retrieve the location information
    # for an IP address, null will be returned.
    if location is None:
        print("Failed to find location.")
    else:
        # Print the Location dictionary.
        print(location)
except Exception as e:
    print(e)
```

#### Look up own location

> For looking up your own location we use https://ip.42.pl/raw

```python
location = geo_lookup.get_own_location()
print(location)
```

#### Other Features

There are also a few other useful features built into this library and the IPStack API.

1. Bulk Location Lookup

   The ipstack API also offers the ability to request data for multiple IPv4 or IPv6 addresses at the same time. This requires the PROFESSIONAL teir API key or higher and is limitted to 50 IPs at a time.
   > See: [https://ipstack.com/documentation#bulk](https://ipstack.com/documentation#bulk)

   ```python
   locations = geo_lookup.get_location("github.com", "stackoverflow.com")
   print(locations)
   ```

2. Requesting the hostname for an IP address.

   By default, the ipstack API does not return information about the hostname the given IP address resolves to. In order to include the hostname use the following.
   > See: [https://ipstack.com/documentation#hostname](https://ipstack.com/documentation#hostname)

   ```python
   location = geo_lookup.find_hostname().get_location("1.1.1.1")
   print(location["hostname"])
   ```

   ```
   one.one.one.one
   ```

3. Assessing Security

   Customers subscribed to the Professional Plus Plan may access the ipstack API's Security Module, which can be used to assess risks and threats originating from certain IP addresses before any harm can be done to a website or web application.
   > See: [https://ipstack.com/documentation#security](https://ipstack.com/documentation#security)

   ```python
   location = geo_lookup.assess_security().get_location("github.com")
   ```

4. Set the language for a response

   The ipstack API is capable of delivering its result set in different languages. To request data in a language other than English (default) use following with one of the supported language codes.
   > See: [https://ipstack.com/documentation#language](https://ipstack.com/documentation#language)

   [Supported Langauges](https://ipstack.com/documentation#language)

   ```python
   location = geo_lookup.language("en").get_location("github.com")
   ```

5. Configuring your request

   ```python
   # Use HTTPS
   # This requires IPStack Basic plan or higher.
   location = geo_lookup.use_https().get_location("github.com")

   # Configure the timeout for requests
   location = geo_lookup.timeout(10).get_location("github.com")
   ```

### Development

Before commiting anything, please create a pre-commit hook with the following content.

This will ensure that the pycodestyle badge is properly updated.

```bash
#!/bin/bash
python3 tests/style.py
```

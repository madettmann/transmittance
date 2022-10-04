From source:

- clone this repo
- run `source bin/activate` to activate the environment
- add this directory to your path
- run `transmittance` from a directory containing directories of power data and temperature data

From Docker:

- Install docker https://docs.docker.com/engine/install/
- Run `docker pull madettmann/transmittance:latest` to pull the latest version
- Run `docker run -v $(pwd):/app madettmann/transmittance` from a directory containing directories of power data and temperature data

Here is the folder structure

```cwd
--|1090
--|--|Power1090.txt
--|--|Tdiss1090.txt
--|2080
--|--|Power2080.txt
--|--|Tdiss2080.txt
--|3070
--|--|Power3070.txt
--|--|Tdiss3070.txt
--|.
--|.
--|.
```

Here the number is a folder representing the ratio of solvents. Tdiss is the temperature measurement file and Power is the power meter file.

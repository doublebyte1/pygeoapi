.. _ogcapi-edr:

Publishing data to OGC API - Environmental Data Retrieval
=========================================================

The `OGC Environmental Data Retrieval (EDR) (API)`_ provides a family of
lightweight query interfaces to access spatio-temporal data resources.

To add spatio-temporal data to pygeoapi for EDR query interfaces, you
can use the dataset example in :ref:`configuration` as a baseline and
modify accordingly.

Providers
---------

pygeoapi core EDR providers are listed below, along with a matrix of supported query
types and query arguments.

.. csv-table::
   :header: Provider, Position, Radius, Area, Cube, Trajectory, Corridor, Items, Locations, Instances
   :align: left

   `xarray-edr`_,✅,❌,❌,✅,❌,❌,❌,❌,❌
   `SensorThingsEDR`_,❌,❌,✅,✅,❌,❌,✅,✅,❌


.. csv-table::
   :header: Provider, coords, parameter-name, datetime
   :align: left

   `xarray-edr`_,✅,✅,✅
   `SensorThingsEDR`_,✅,✅,✅


Below are specific connection examples based on supported providers.

Connection examples
-------------------

xarray-edr
^^^^^^^^^^

.. note::
   Requires Python package xarray

The `xarray-edr`_ provider plugin reads and extracts `NetCDF`_ and `Zarr`_ data via `xarray`_.

.. code-block:: yaml

   providers:
       - type: edr
         name: xarray-edr
         data: tests/data/coads_sst.nc
         # optionally specify x/y/time fields, else provider will attempt
         # to derive automagically
         x_field: lon
         y_field: lat
         z_field: z
         time_field: time
         # optionally specify the coordinate reference system of your dataset
         # else pygeoapi assumes it is WGS84 (EPSG:4326).
         storage_crs: 4326
         format:
            name: netcdf
            mimetype: application/x-netcdf

   providers:
       - type: edr
         name: xarray-edr
         data: tests/data/analysed_sst.zarr
         format:
            name: zarr
            mimetype: application/zip
    
    providers:
       - type: edr
         name: xarray-edr
         data: s3://power-analysis-ready-datastore/power_901_annual_meteorology_utc.zarr
         format:
            name: zarr
            mimetype: application/zip
         options:
            s3:
               anon: true
               requester_pays: false

.. note::

   `Zarr`_ files are directories with files and subdirectories.  Therefore
   a zip file is returned upon request for said format.

.. note::
   When referencing data stored in an S3 bucket, be sure to provide the full
   S3 URL. Any parameters required to open the dataset using fsspec can be added
   to the config file under `options` and `s3`, as shown above.

.. note::
   When providing a `storage_crs` value in the EDR configuration, specify the 
   coordinate reference system using any valid input for 
   `pyproj.CRS.from_user_input`_. 


SensorThingsEDR
^^^^^^^^^^^^^^^

The SensorThings API EDR Provider for pygeaopi extends the feature provider to
produce CoverageJSON representations from SensorThings responses repsonses. This provider
relies on using the ObservedProperty Entity to create the `parameter-name` set.

.. code-block:: yaml

   providers:
      - type: edr
        name: SensorThingsEDR
        data: https://emotional.byteroad.net/FROST-Server/v1.1/
      - type: feature
        name: SensorThings
        data: https://emotional.byteroad.net/FROST-Server/v1.1/Things
        title_field: name


.. note::
   The `feature` provider must also be configured to service the `.../items` 
   EDR query type.


Data access examples
--------------------

* list all collections

  * http://localhost:5000/collections
* overview of dataset

  * http://localhost:5000/collections/foo
* dataset position query

  * http://localhost:5000/collections/foo/position?coords=POINT(-75%2045)
* dataset position query for a specific parameter

  * http://localhost:5000/collections/foo/position?coords=POINT(-75%2045)&parameter-name=SST
* dataset position query for a specific parameter and time step

  * http://localhost:5000/collections/foo/position?coords=POINT(-75%2045)&parameter-name=SST&datetime=2000-01-16


.. _`xarray`: https://docs.xarray.dev/en/stable/
.. _`NetCDF`: https://en.wikipedia.org/wiki/NetCDF
.. _`Zarr`: https://zarr.readthedocs.io/en/stable
.. _`pyproj.CRS.from_user_input`: https://pyproj4.github.io/pyproj/stable/api/crs/coordinate_system.html#pyproj.crs.CoordinateSystem.from_user_input
.. _`OGC Environmental Data Retrieval (EDR) (API)`: https://ogcapi.ogc.org/edr

from netCDF4 import Dataset


def test_coring_data_netcdf(nc_file):
    ncfile = Dataset(nc_file, 'r')

    num_sheets = len(ncfile.dimensions['sheet'])
    for i in range(num_sheets):
        print("\nFeuille", i+1)
        print("Core Number:", ncfile.variables['core_number'][i])
        print("Investigator:", ncfile.variables['investigator'][i])
        print("Date:", ncfile.variables['date'][i])
        print("Time:", ncfile.variables['time'][i])
        print("Location:", ncfile.variables['location'][i])
        print("Location Comments:", ncfile.variables['location_comments'][i])
        print("Air Temp:", ncfile.variables['air_temp'][i])
        print("Snow Surface Temp:", ncfile.variables['snow_surface_temp'][i])
        print("Ice-Snow Interface Temp:", ncfile.variables['ice_snow_interface_temp'][i])
        print("Snow Depth:", ncfile.variables['snow_depth'][i])
        print("Ice Thickness:", ncfile.variables['ice_thickness'][i])
        print("Freeboard:", ncfile.variables['freeboard'][i])
        print("Sample Bucket:", ncfile.variables['sample_bucket'][i])
        print("Comments:", ncfile.variables['comments'][i])

        print("\nDonnées de mesure :")
        for var_name in ncfile.variables:
            if var_name not in ['core_number', 'investigator', 'date', 'time', 'location', 'location_comments',
                                'air_temp', 'snow_surface_temp', 'ice_snow_interface_temp', 'snow_depth',
                                'ice_thickness', 'freeboard', 'sample_bucket', 'comments']:
                print(var_name.replace('_', ' '), ":", ncfile.variables[var_name][i][:])



test_coring_data_netcdf('ICE_CORES_DATA_RAW_2024.nc')

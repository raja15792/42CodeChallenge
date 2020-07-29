# 42CodeChallenge

More information [here](https://gist.github.com/surjikal/3c8b21f4ffe92e1af299)

# Solution:

The solution has been divided into 4 parts:
- Reading the file
	Reading from the input file, given as argument, line by line 
- Building Global Property Map and creating row **dict**
    The Global `PROPERTY_MAP` is being build to define the group within that property.
    For the given example in the challenge the property map looks like:
    ```json
    {
    	'$total': {
    		'$total': {
    			'net_sales': '200'
    		}
    	},
    	'foo': {
    		'$total': {
    			'net_sales': '400'
    		},
    		'bacon': {
    			'net_sales': '100'
    		},
    		'sauce': {
    			'net_sales': '300'
    		}
    	},
    	'bar': {
    		'bro': {
    			'net_sales': '200'
    		},
    		'$total': {
    			'net_sales': '-200'
    		},
    		'sup': {
    			'net_sales': '-400'
    		}
    	}
    }
    ```
    Similary build the dict of each row where the **key** is **property/metric name** and **value** is the value in that row.
    ```json
    {'property0': 'bar', 'property1': '$total', 'net_sales': '-200'}
    ```
- Sorting using the Global Property Map
    Defined custom compare function that returns an integer denoting whether first argument is bigger, smaller or equal to the second argument.
    Now for given two rows the compare function will compare the property values 
        - if they belong to the same group and any one of the property value is `$total` then returing `-1` to denote its smaller than the other argument/row.
        - if belong to same group, traverse the `PROPERTY_MAP` till reach the metric to compare and sort based on that metric value
        - otherwise if don't belong to the same group, compare the `$total` value of the metric to determine the order.
- Writing to the file
    Writing to the output file, which is given as argument, piping the `row ` dict


# To Run

```
python index.py --input_file <input_file_location> --output_file <output_file_location> --metric <metric_to_compare>
```	

# Example

```
python index.py --input_file data.txt --output_file output.txt --metric net_sales
````	

initialPheromoneLevel = (1)

graph= {
    'a' : [{
            'name': 'b',
            'distance' : 2,
            'pheromones':initialPheromoneLevel
        },
        {
            'name': 'd',
            'distance' : 12,
            'pheromones':initialPheromoneLevel
        },
        {
            'name': 'e',
            'distance' : 5,
            'pheromones':initialPheromoneLevel
        
    }],
    'b' : [{
            'name': 'a',
            'distance' : 2,
            'pheromones':initialPheromoneLevel
        },
        {
            'name': 'd',
            'distance' : 8,
            'pheromones':initialPheromoneLevel
        },
        {
            'name': 'c',
            'distance' : 4,
            'pheromones':initialPheromoneLevel
    }],
    'c' : [{
            'name': 'd',
            'distance' : 3,
            'pheromones':initialPheromoneLevel
        },
        {
            'name': 'e',
            'distance' : 3,
            'pheromones':initialPheromoneLevel
        },
        {
            'name': 'b',
            'distance' : 4,
            'pheromones':initialPheromoneLevel
    }],
    'd' : [{
            'name': 'a',
            'distance' : 12,
            'pheromones':initialPheromoneLevel
        },
        {
            'name': 'b',
            'distance' : 8,
            'pheromones':initialPheromoneLevel
        },
        {
            'name': 'c',
            'distance' : 3,
            'pheromones':initialPheromoneLevel
        },
        {
            'name': 'e',
            'distance' : 10,
            'pheromones':initialPheromoneLevel
    }],
    'e' : [{
            'name': 'a',
            'distance' : 5,
            'pheromones':initialPheromoneLevel
        },
        {
            'name': 'c',
            'distance' : 3,
            'pheromones':initialPheromoneLevel
        },
        {
            'name': 'd',
            'distance' : 10,
            'pheromones':initialPheromoneLevel
    }],
       
}


graph15 = {
  "a": [
    {
      "name": "b",
      "distance": 4,
      "pheromones": initialPheromoneLevel
    },
    {
      "name": "c",
      "distance": 17,
      "pheromones": initialPheromoneLevel
  }],
  "b": [
    {
      "name": "a",
      "distance": 4,
      "pheromones": initialPheromoneLevel
    },
    {
      "name": "e",
      "distance": 2,
      "pheromones": initialPheromoneLevel
    }
  ],
  "c": [
    {
      "name": "a",
      "distance": 17,
      "pheromones": initialPheromoneLevel
    },
    {
      "name": "d",
      "distance": 3,
      "pheromones": initialPheromoneLevel
    }
  ],
  "d": [
    {
      "name": "c",
      "distance": 3,
      "pheromones": initialPheromoneLevel
    },
    
    {
      "name": "g",
      "distance": 2,
      "pheromones": initialPheromoneLevel
    },
    
    {
      "name": "j",
      "distance": 7,
      "pheromones": initialPheromoneLevel
    }
  ],
  "e": [
    {
      "name": "b",
      "distance": 2,
      "pheromones": initialPheromoneLevel
    },
    
    {
      "name": "f",
      "distance": 4,
      "pheromones": initialPheromoneLevel
    }
  ],
  "f": [
    {
      "name": "e",
      "distance": 4,
      "pheromones": initialPheromoneLevel
    },
    
    {
      "name": "g",
      "distance": 3,
      "pheromones": initialPheromoneLevel
    },
    {
      "name": "h",
      "distance": 14,
      "pheromones": initialPheromoneLevel
    },
    {
      "name": "i",
      "distance": 2,
      "pheromones": initialPheromoneLevel
    }
    
  ],
  "g": [
    {
      "name": "d",
      "distance": 2,
      "pheromones": initialPheromoneLevel
    },
    {
      "name": "f",
      "distance": 3,
      "pheromones": initialPheromoneLevel
    },
    
    {
      "name": "h",
      "distance": 7,
      "pheromones": initialPheromoneLevel
    },
    {
      "name": "j",
      "distance": 11,
      "pheromones": initialPheromoneLevel
    }
  ],
  "h": [
    {
      "name": "f",
      "distance": 14,
      "pheromones": initialPheromoneLevel
    },
    {
      "name": "g",
      "distance": 7,
      "pheromones": initialPheromoneLevel
    },
    
    {
      "name": "i",
      "distance": 2,
      "pheromones": initialPheromoneLevel
    },
    
  ],
  "i": [
    {
      "name": "h",
      "distance": 2,
      "pheromones": initialPheromoneLevel
    },
    {
      "name": "m",
      "distance": 4,
      "pheromones": initialPheromoneLevel
    }
  ],
  "j": [
    {
      "name": "d",
      "distance": 7,
      "pheromones": initialPheromoneLevel
    },
    {
      "name": "g",
      "distance": 11,
      "pheromones": initialPheromoneLevel
    },
    {
      "name": "k",
      "distance": 8,
      "pheromones": initialPheromoneLevel
    }
  ],
  "k": [
    {
      "name": "j",
      "distance": 8,
      "pheromones": initialPheromoneLevel
    },
    
    {
      "name": "l",
      "distance": 7,
      "pheromones": initialPheromoneLevel
    }
  ],
  "l": [
    {
      "name": "k",
      "distance": 7,
      "pheromones": initialPheromoneLevel
    },
    
    {
      "name": "n",
      "distance": 2,
      "pheromones": initialPheromoneLevel
    }
  ],
  "m": [
    {
      "name": "i",
      "distance": 4,
      "pheromones": initialPheromoneLevel
    },
    {
      "name": "o",
      "distance": 6,
      "pheromones": initialPheromoneLevel
    }
  ],
  "n": [ 
    {
      "name": "l",
      "distance": 2,
      "pheromones": initialPheromoneLevel
    },
  
    {
      "name": "o",
      "distance": 4,
      "pheromones": initialPheromoneLevel
    }
  ],
  "o": [
    {
      "name": "m",
      "distance": 6,
      "pheromones": initialPheromoneLevel
    },
    {
      "name": "n",
      "distance": 4,
      "pheromones": initialPheromoneLevel
    }
  ],
}
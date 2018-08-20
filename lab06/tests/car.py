test = {
  'name': 'Car',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> from car import *
          >>> hilfingers_car = Car('Tesla', 'Model S')
          >>> hilfingers_car.color
          058a4899e0e4f451de8b35121de08b60
          # locked
          >>> hilfingers_car.paint('black')
          984dff86cb2343e4e5b0486c439464d8
          # locked
          >>> hilfingers_car.color
          e74918d4310bb6cbc896676f20dc20de
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> from car import *
          >>> hilfingers_car = Car('Tesla', 'Model S')
          >>> hilfingers_truck = MonsterTruck('Monster Truck', 'XXL')
          >>> hilfingers_car.size
          77680819e28d50de159e07d024a1683f
          # locked
          >>> hilfingers_truck.size
          07bd1cf0e022b8f011a9680a683d13e2
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> from car import *
          >>> hilfingers_car = Car('Tesla', 'Model S')
          >>> hilfingers_car.model
          74c2147b5ba7769cc5f991cbfd7b8d69
          # locked
          >>> hilfingers_car.gas = 10
          >>> hilfingers_car.drive()
          1a050ef9b8e68b745fd1986a9eba405f
          # locked
          >>> hilfingers_car.drive()
          568957c82681d74b2e26961d417b2328
          # locked
          >>> hilfingers_car.fill_gas()
          9b8d79d813de2e0e75ecc60353933fc3
          # locked
          >>> hilfingers_car.gas
          9ff3fc64d351fcb9f34aaafe02363c3e
          # locked
          >>> Car.gas
          1987bce9c137ee1be913e29126e18d3c
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> from car import *
          >>> hilfingers_car = Car('Tesla', 'Model S')
          >>> Car.headlights
          d05bc830613dfa69ef96df4f94a8da70
          # locked
          >>> hilfingers_car.headlights
          d05bc830613dfa69ef96df4f94a8da70
          # locked
          >>> Car.headlights = 3
          >>> hilfingers_car.headlights
          214f1f0cf62380259278c29f0dd9185d
          # locked
          >>> hilfingers_car.headlights = 2
          >>> Car.headlights
          214f1f0cf62380259278c29f0dd9185d
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> from car import *
          >>> hilfingers_car = Car('Tesla', 'Model S')
          >>> hilfingers_car.wheels = 2
          >>> hilfingers_car.wheels
          d05bc830613dfa69ef96df4f94a8da70
          # locked
          >>> Car.num_wheels
          41cc26e29cc2a9e0b6fb880e349243bb
          # locked
          >>> hilfingers_car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          568957c82681d74b2e26961d417b2328
          # locked
          >>> Car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          34db8258c24aff02f4e0aeaa32af407b
          # locked
          >>> Car.drive(hilfingers_car) # Type Error if an error occurs and Nothing if nothing is displayed
          568957c82681d74b2e26961d417b2328
          # locked
          >>> MonsterTruck.drive(hilfingers_car) # Type Error if an error occurs and Nothing if nothing is displayed
          34db8258c24aff02f4e0aeaa32af407b
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          >>> from car import *
          >>> deneros_car = MonsterTruck('Monster', 'Batmobile')
          >>> deneros_car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
          238e48b17a8085331a1d671045b7a572
          fb0f2e56ddf6ff5ff7ad283bc4036c42
          # locked
          >>> Car.drive(deneros_car) # Type Error if an error occurs and Nothing if nothing is displayed
          fb0f2e56ddf6ff5ff7ad283bc4036c42
          # locked
          >>> MonsterTruck.drive(deneros_car) # Type Error if an error occurs and Nothing if nothing is displayed
          238e48b17a8085331a1d671045b7a572
          fb0f2e56ddf6ff5ff7ad283bc4036c42
          # locked
          >>> Car.rev(deneros_car) # Type Error if an error occurs and Nothing if nothing is displayed
          34db8258c24aff02f4e0aeaa32af407b
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}

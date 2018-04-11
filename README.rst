aioworkers-attrs
================


mymodule.py:

.. code-block:: python

  from aioworkers_attrs import attr


  @attr.entity
  class A:
      c = attr.ib(type=int)

      @c.default
      def set_default_c(self):
          return self.config.get('c', 0)


conf.yaml:

.. code-block:: yaml

  a:
    cls: mymodule.A
    c: 1


run:

.. code-block:: bash

  aioworkers -i -c conf.yaml


and type:

.. code-block:: python

  > from aioworkers_attrs import attr

  > attr.asdict(context.a)

  {'c': 1}

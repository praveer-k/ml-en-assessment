Architecture
===========================

Following uml diagram shows the communication between all the actors involved in running the process.

.. uml:: ../_diagrams/sequence.puml
    :alt: Diagram to show various actors invovled and there interactions
    :align: center
    :height: 20em

So, in essence, the user triggers various functions by sending the command to:

    - load, clean and aggregate data.
    - categorzie to extract text based information from the properties and description.
    - show dashboard that fetches data which can now be shown as stats.
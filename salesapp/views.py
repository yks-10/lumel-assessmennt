import csv

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from salesapp.models import Customer, Order, Product
from salesapp.serializers import CustomerSerializer, OrderSerializer, ProductSerializer

class HealthView(APIView):
    def get(self, request):
        """
            @description: This API used to check if server is active or not
            @param request:
            @return: "SUCCESS"
        """
        response = {"status": "success"}
        return Response(response)


class CustomerView(APIView):
    def get(self, request):
        """
           @description: This API used to get all customer
           @param request:
           @return: "SUCCESS"
        """

        try:
            data = request.data
            if data:
                name = data.get('name')
                detail = Customer.objects.get(name=name)
                serializer = CustomerSerializer(detail)
            else:
                detail = Customer.objects.all()
                serializer = CustomerSerializer(detail, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)


    def post(self, request):
        """
           @description: This API used to create customer
           @param request: name, email, address
           @return: "SUCCESS"
        """

        try:
            data = request.data
            name = data.get('name')
            email = data.get('email')
            address = data.get('address')
            Customer.objects.create(name=name, email=email, address=address)
            response = {"status": "success"}
            return Response(response)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        """
          @description: This API used to update customer
          @param request: data
          @return: "SUCCESS"
       """
        try:
            data = request.data
            name = data.get('name')
            email = data.get('email')
            address = data.get('address')
            customer = Customer.objects.get(name=name)
            customer.name = name
            customer.email = email
            customer.address = address
            customer.save()
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request):
        """
             @description: This API used to delete customer
             @param request: date
             @return: "SUCCESS"
        """
        try:
            data = request.data
            name = data.get('name')
            customer = Customer.objects.get(name=name)
            customer.delete()
            response = {"status": "Customer deleted successfully"}
            return Response(response)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

class ProductView(APIView):
    def get(self, request):
        """
           @description: This API used to get all Products
           @param request:
           @return: "SUCCESS"
        """

        try:
            data = request.data
            if data:
                id = data.get('id')
                detail = Product.objects.get(pk=id)
                serializer = ProductSerializer(detail)
            else:
                detail = Product.objects.all()
                serializer = ProductSerializer(detail, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        """
           @description: This API used to create product
           @param request: data
           @return: "SUCCESS"
        """

        try:
            data = request.data
            product_name = data.get('product_name')
            categories = data.get('categories')
            sale_date = data.get('sale_date')
            unit_price = data.get('unit_price')
            discount = data.get('discount')
            Product.objects.create(product_name=product_name, categories=categories, sale_date=sale_date, unit_price=unit_price, discount=discount)
            response = {"status": "product created successfully"}
            return Response(response)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        """
             @description: This API used to delete Product
             @param request: date
             @return: "SUCCESS"
        """
        try:
            data = request.data
            id = data.get('id')
            product = Product.objects.get(pk=id)
            product.delete()
            response = {"status": "Product deleted successfully"}
            return Response(response)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)


class OrderView(APIView):
    def get(self, request):
        """
           @description: This API used to get all order
           @param request:
           @return: "SUCCESS"
        """

        try:
            data = request.data
            if data:
                id = data.get('id')
                detail = Order.objects.get(pk=id)
                serializer = OrderSerializer(detail)
            else:
                detail = Order.objects.all()
                serializer = OrderSerializer(detail, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        """
           @description: This API used to create order
           @param request: data
           @return: "SUCCESS"
        """

        try:
            data = request.data
            shipment_cost = data.get('shipment_cost')
            payment_type = data.get('payment_type')
            quantity_sold = data.get('quantity_sold')
            product_id = data.get('product')
            product = get_object_or_404(Product, pk=product_id)
            x = Order.objects.create(shipment_cost=shipment_cost, payment_type=payment_type, quantity_sold=quantity_sold, product=product)
            print(x,"hii")
            response = {"status": "order created successfully"}
            return Response(response)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        """
             @description: This API used to delete order
             @param request: date
             @return: "SUCCESS"
        """
        try:
            data = request.data
            id = data.get('id')
            order = Order.objects.get(pk=id)
            order.delete()
            response = {"status": "Order deleted successfully"}
            return Response(response)
        except Exception as e:
            return Response(e, status=status.HTTP_400_BAD_REQUEST)


class DataImport(APIView):
    def get(self, request):
        try:
            def import_data(file_path):
                with open(file_path, 'r') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        name = row['name'],
                        email = row['email'],
                        address = row['address']
                        customer = Customer.objects.get(name=name)
                        if not customer:
                            Customer.objects.create(name=name, email=email, address=address)
            csv_file_path = '/home/yogesh/Documents/lumel/salesdata/data.csv'
            import_data(csv_file_path)
            response = {"status": "Data imported successfully"}
            return Response(response)
        except Exception as e:
            response = {"status": "Data imported successfully"}
            return Response(response)

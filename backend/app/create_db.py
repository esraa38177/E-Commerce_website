from backend.app import app
from backend.models import db, Product

with app.app_context():
    db.create_all()

    # Add sample products
    product1 = Product(name='Fresh Milk', description='1L organic milk.', price=3.99, image_file='milk.jpg')
    product2 = Product(name='Red Apple', description='Sweet and crispy apples.', price=0.99, image_file='apple.jpg')
    product3 = Product(name='Whole Wheat Bread', description='Healthy and fresh.', price=2.49, image_file='bread.jpg')

    db.session.add_all([product1, product2, product3])
    db.session.commit()

    print("✅ Database created and products added.")

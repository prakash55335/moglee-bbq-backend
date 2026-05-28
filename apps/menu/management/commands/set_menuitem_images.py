from django.core.management.base import BaseCommand
from apps.menu.models import MenuItem


class Command(BaseCommand):
    help = 'Set HD images for all Mr. Moglee menu items'

    def handle(self, *args, **kwargs):

        item_images = {

            # BBQ Chicken
            'Chicken Drumstick (1 Pc)':           'https://images.unsplash.com/photo-1655463485347-f3dd84fead5b?fm=jpg&q=60&w=3000&auto=format&fit=crop',
            'Chicken Drumstick (2 Pcs)':          'https://images.pexels.com/photos/13823476/pexels-photo-13823476.jpeg?cs=srgb&dl=pexels-footage-kingdom-122917970-13823476.jpg&fm=jpg',
            'Chicken Lollipops (3 Pcs)':          'https://images.unsplash.com/photo-1626645738196-c2a7c87a8f58?w=800&q=90',
            'Chicken Lollipops (5 Pcs)':          'https://static.vecteezy.com/system/resources/thumbnails/053/286/945/small/golden-chicken-fry-perfection-with-stunning-background-bokeh-effects-photo.jpg',
            'Chicken Wings (3 Pcs)':              'https://images.unsplash.com/photo-1624153064067-566cae78993d?fm=jpg&q=60&w=3000&auto=format&fit=crop',
            'Chicken Wings (5 Pcs)':              'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTxZztFhYkNf4_wIGe_Ju4RoWwV7uoKT6uTwQ&s',
            'Chicken Strips (4 Pcs)':             'https://www.shutterstock.com/image-photo/chicken-fingers-breaded-fried-strips-600nw-2549056017.jpg',
            'Chicken Strips (6 Pcs)':             'https://thumbs.dreamstime.com/b/ai-generative-image-chicken-tenders-crispy-breaded-chicken-strips-golden-brown-delicious-perfect-dipping-281162993.jpg',
            'Peri Peri Chicken Leg (3 Pcs)':      'https://static.vecteezy.com/system/resources/thumbnails/067/168/530/small/spicy-grilled-chicken-legs-a-culinary-delight-free-png.png',
            'Peri Peri Chicken Leg (5 Pcs)':      'https://www.licious.in/blog/wp-content/uploads/2020/12/Peri-Peri-Chicken-at-home.jpg',

            # Pepper BBQ Chicken
            'Pepper BBQ Chicken (1 Pc)':          'https://www.a2zshoppy.com/media/image?path=uploads/media/2025/bbqchickenpepper_a2z_shoppy.jpg&width=800&quality=80',
            'Pepper BBQ Chicken (2 Pcs)':         'https://static.vecteezy.com/system/resources/thumbnails/074/383/880/small/a-plate-of-chicken-wings-with-a-dipping-sauce-photo.jpeg',
            'Pepper BBQ Chicken (4 Pcs)':         'https://easychickenrecipes.com/wp-content/uploads/2023/06/grilled-bbq-chicken-recipe-1-of-7-edited.jpg',
            'Pepper BBQ Chicken (8 Pcs)':         'https://plus.unsplash.com/premium_photo-1692835633701-ad06af67cec7?fm=jpg&q=60&w=3000&auto=format&fit=crop',
            'Pepper BBQ Chicken (12 Pcs)':        'https://images.unsplash.com/photo-1700135893698-6b8a048a0cf9?fm=jpg&q=60&w=3000&auto=format&fit=crop',

            # Sea Food
            'Sankara Fish':                       'https://thumbs.dreamstime.com/b/fried-fish-shrimp-dinner-cole-slaw-97530907.jpg',
            'BBQ Fish Slice':                     'https://static.vecteezy.com/system/resources/thumbnails/040/164/446/small/ai-generated-a-sizzling-fish-on-the-grill-flames-dancing-around-the-freshly-cooked-catch-photo.jpeg',
            'Full BBQ Fish (Bhasa)':              'https://ik.imagekit.io/iwcam3r8ka/prod/blog-header/202501/4b42ba1e-8d5c-4a39-8969-6b52a500f274.jpg',
            'Prawn (5 Pcs)':                      'https://media.istockphoto.com/id/2246700873/photo/shrimp-tempura-with-chili-sauce-on-a-black-plate-dark-grey-background-close-up.jpg?s=612x612&w=0&k=20&c=uX-IlqhJtv_q-3KMz87MDVxG2b1DOy23QMRphEtzOV0=',
            'Prawn (10 Pcs)':                     'https://media.istockphoto.com/id/2246700629/photo/closeup-of-tempura-shrimp-on-a-black-plate-dark-grey-background-close-up.jpg?s=612x612&w=0&k=20&c=buFd665cu0itYoP38MUvOyagRc7iA3NAWcYrobVqDVE=',

            # Veg BBQ
            'Paneer (5 Pcs)':                     'https://t4.ftcdn.net/jpg/18/05/25/31/360_F_1805253185_P8n3huCNFkzuOm7d0oYv5cdXuVGz5Vdq.jpg',
            'Pineapple (4 Pcs)':                  'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT2WF19lZDDF0leeS13O2qyotOqqOA1cHFt2Q&s',

            # Celebration Pack
            'Wings Bucket (10 Pcs)':              'https://img.freepik.com/premium-photo/fried-chicken-wings-legs-bucket-full-crispy-kentucky-fried-chicken-brown-background_79782-13625.jpg',
            'Wings Bucket (20 Pcs)':              'https://thumbs.dreamstime.com/b/crispy-fried-chicken-bucket-food-photography-fast-wings-330649956.jpg',
            'Lollipop Bucket (10 Pcs)':           'https://t3.ftcdn.net/jpg/17/14/20/12/360_F_1714201231_PPsxpNn374F4Z8IjlWMCDMjXYE72Xp9D.jpg',
            'Lollipop Bucket (20 Pcs)':           'https://st3.depositphotos.com/7691758/17463/i/450/depositphotos_174638242-stock-photo-deep-fried-crispy-tasty-chicken.jpg',

            # Burger Combos
            'Veg Burger Combo':                   'https://images.unsplash.com/photo-1550547660-d9450f859349?w=800&q=90',
            'Chicken Fillet Burger Combo':        'https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=800&q=90',
            'Fish Fillet Burger Combo':           'https://images.unsplash.com/photo-1594212699903-ec8a3eca50f5?w=800&q=90',

            # Wings Combos
            '5 PCS Wings Combo':                  'https://media.istockphoto.com/id/1369101558/photo/plate-of-barbecue-chicken-wings-top-view.jpg?s=612x612&w=0&k=20&c=cFFVf7PwTtcIgOFsIVh4gOlCr-lyzhUhH9Y91e8Sr0Q=',
            '10 PCS Wings Combo':                 'https://img.freepik.com/free-photo/baked-chicken-wings-asian-style_2829-10160.jpg?semt=ais_incoming&w=740&q=80',
            '20 PCS Wings Combo':                 'https://images.unsplash.com/photo-1624153064067-566cae78993d?fm=jpg&q=60&w=3000&auto=format&fit=crop',

            # Lollipop Combos
            '5 PCS Lollipop Combo':               'https://images.unsplash.com/photo-1626645738196-c2a7c87a8f58?w=800&q=90',
            '10 PCS Lollipop Combo':              'https://t3.ftcdn.net/jpg/04/07/37/94/360_F_407379443_KIdJDRuKDLOSLNT93VN3PfFh8hzGEO9P.jpg',
            '20 PCS Lollipop Combo':              'https://t3.ftcdn.net/jpg/17/34/76/42/360_F_1734764232_WK2QTiMwRMbXTzvn0Ufw2xPrYVXSqrbh.jpg',

            # Special Combo
            'Party Pack':                         'https://images.unsplash.com/photo-1529543544282-ea669407fca3?w=800&q=90',
            'Birthday Pack':                      'https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=800&q=90',

            # Starters
            'French Fries (R)':                   'https://images.unsplash.com/photo-1573080496219-bb080dd4f877?w=800&q=90',
            'French Fries (L)':                   'https://images.unsplash.com/photo-1541592106381-b31e9677c0e5?w=800&q=90',
            'Peri Peri Fries (R)':                'https://images.unsplash.com/photo-1630431341973-02e1b662ec35?w=800&q=90',
            'Peri Peri Fries (L)':                'https://static.vecteezy.com/system/resources/thumbnails/039/628/088/small/ai-generated-healthy-grilled-meat-and-vegetable-plate-with-fresh-salad-generated-by-ai-photo.jpg',
            'Veg Nuggets':                        'https://images.unsplash.com/photo-1562967914-608f82629710?w=800&q=90',
            'Veg Cheesy Balls (5 Pcs)':           'https://scbsgroup.in/wp-content/uploads/2025/07/Cheese-Balls.jpg',
            'Cheese Corn Nuggets (5 Pcs)':        'https://www.desicooks.com/dms/images/cnc2---a.jpg',
            'Veg Fried Roll (5 Pcs)':             'https://t3.ftcdn.net/jpg/00/89/95/08/360_F_89950874_LVsh6xkVvHEPZUqH60qZRkUq5VNfsba3.jpg',
            'Fried Paneer Momos':                 'https://thumbs.dreamstime.com/b/garnished-steam-paneer-momos-cafe-289398240.jpg',
            'Fried Chicken Momos':                'https://img.freepik.com/premium-photo/chicken-pan-fried-momo_943281-78183.jpg?w=740',
            'Chicken Pops (100g)':                'https://t4.ftcdn.net/jpg/04/59/22/95/360_F_459229574_sbcmzJHsWoGG0Nd0JK8qZsCp7dd78JRb.jpg',
            'Chicken Cheese Pops (5 Pcs)':        'https://derafarms.com/cdn/shop/files/deraproducts_94.png?v=1717672219',
            'Chicken Nuggets (5 Pcs)':            'https://static.onfast.app/merchant/m_juicemonkey/product/63/0-2021-02-05T12:46:56.760894.jpg',

            # Moglee Fried Chicken
            'Chicken Wings (5 Pcs)':              'https://images.unsplash.com/photo-1637273484026-11d51fb64024?fm=jpg&q=60&w=3000&auto=format&fit=crop',
            'Chicken Lollipop (5 Pcs)':           'https://t3.ftcdn.net/jpg/04/07/37/94/360_F_407379443_KIdJDRuKDLOSLNT93VN3PfFh8hzGEO9P.jpg',
            'Chicken Popcorn (150g)':             'https://www.shutterstock.com/image-photo/crispy-popcorn-chicken-ketchup-sauce-260nw-2464019771.jpg',
            'Fish Strips (4 Pcs)':                'https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?w=800&q=90',
            'Chicken Strips (4 Pcs)':             'https://www.shutterstock.com/image-photo/chicken-fingers-breaded-fried-strips-600nw-2549056017.jpg',
            'Prawns (5 Pcs)':                     'https://thumbs.dreamstime.com/b/kerala-fish-curry-prawns-chemmeen-roast-shrimp-fry-spicy-masala-banana-leaf-plate-dark-black-background-south-india-top-view-198229453.jpg',

            # Burger
            'Veg Burger':                         'https://media.gettyimages.com/id/534321264/photo/gourmet-veggie-burger-with-red-skin-fries.jpg?s=612x612&w=gi&k=20&c=wgi9Af6BHHXami-7LFh9vgoasNbwp3EyIvRkFokVsRs=',
            'Paneer Patty Burger':                'https://images.unsplash.com/photo-1571091718767-18b5b1457add?w=800&q=90',
            'Cheesy Veg Burger':                  'https://images.unsplash.com/photo-1565299507177-b0ac66763828?w=800&q=90',
            'Cheesy Paneer Burger':               'https://images.unsplash.com/photo-1586190848861-99aa4a171e90?w=800&q=90',
            'Chicken Patty Burger':               'https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=800&q=90',
            'Chicken Fillet Burger':              'https://t4.ftcdn.net/jpg/15/96/09/95/360_F_1596099543_IbZQxKOCEHQ2C6cd7ebcaXUy41YMYHoS.jpg',
            'BBQ Chicken Burger':                 'https://images.unsplash.com/photo-1553979459-d2229ba7433b?w=800&q=90',
            'Egg Burger':                         'https://t4.ftcdn.net/jpg/18/88/34/89/360_F_1888348902_NqTys4twsjoXdIAPCJfRRNLYTDZgF3Pr.jpg',
            'Fish Fillet Burger':                 'https://images.unsplash.com/photo-1594212699903-ec8a3eca50f5?w=800&q=90',

            # Extras
            'Extra Kuboos':                       'https://img.freepik.com/premium-photo/pita-flat-bread-set-gray-stone-table-background_249006-19917.jpg?semt=ais_hybrid&w=740&q=80',
            'Extra Cheese':                       'https://images.unsplash.com/photo-1683314573424-b0da0c795a07?fm=jpg&q=60&w=3000&ixlib=rb-4.1.0',
            'Tandoori Mayo':                      'https://i.pinimg.com/474x/48/ed/a9/48eda9d88d180d58df992f91d7bc1607.jpg',
            'Veg Mayo':                           'https://dpointernational.com/wp-content/uploads/2024/08/photo-mayonnaise-isolated-white-background-scaled.jpg',

            # Shawarma
            'Chicken Shawarma Roll':              'https://thumbs.dreamstime.com/b/close-up-freshly-made-delicious-chicken-shawarma-roll-close-up-freshly-made-delicious-chicken-shawarma-roll-wrapped-390126911.jpg',
            'Chicken Shawarma Plate':             'https://png.pngtree.com/thumb_back/fh260/background/20240525/pngtree-arabic-chicken-shawarma-generate-ai-image_15729960.jpg',
            'Fried Shawarma Roll':                'https://img.freepik.com/premium-photo/fresh-smoky-grilled-chicken-tortilla-wrap-with-fire-french-fries-dark-background_1091270-59443.jpg?w=740&q=80',
            'Fried Shawarma Plate':               'https://img.freepik.com/premium-photo/fresh-smoky-grilled-chicken-tortilla-wrap-with-fire-french-fries-dark-background_1091270-60797.jpg?semt=ais_incoming&w=740&q=80',
            'Paneer Shawarma Roll':               'https://img.freepik.com/premium-photo/kolkatastyle-paneer-kathi-roll-classic-cottage-cheese-wrap_861171-11514.jpg?semt=ais_incoming&w=740&q=80',
            'Paneer Shawarma Plate':              'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=800&q=90',
            'Veg Shawarma Roll':                  'https://static.vecteezy.com/system/resources/previews/067/014/378/non_2x/beef-and-chicken-shawarma-close-upgraphy-free-photo.jpg',
            'Veg Shawarma Plate':                 'https://images.unsplash.com/photo-1561651823-34feb02250e4?w=800&q=90',

            # Sandwich
            'Veg Sandwich':                       'https://images.unsplash.com/photo-1553909489-cd47e0907980?w=800&q=90',
            'Paneer Sandwich':                    'https://images.unsplash.com/photo-1528735602780-2552fd46c7af?w=800&q=90',
            'Corn Sandwich':                      'https://images.unsplash.com/photo-1619096252214-ef06c45683e3?w=800&q=90',
            'Veg Cheesy Sandwich':                'https://plus.unsplash.com/premium_photo-1739906393226-9978e7943b00?fm=jpg&q=60&w=3000&auto=format&fit=crop',
            'Chicken Sandwich':                   'https://img.freepik.com/premium-photo/delicious-crispy-chicken-sandwich_186666-9240.jpg',
            'Egg Sandwich':                       'https://t4.ftcdn.net/jpg/04/82/14/91/360_F_482149176_6X2UsMGRPHgP3FkL0vwnv9xDMqOhH43c.jpg',

            # Ice Cream
            'Vanilla Ice Cream (2 Scoops)':       'https://images.unsplash.com/photo-1598268121084-c8f7126e0cef?w=800&q=90',
            'Vanilla Ice Cream (3 Scoops)':       'https://static.vecteezy.com/system/resources/thumbnails/040/274/180/small/ai-generated-vanilla-ice-cream-scoops-on-white-background-free-photo.jpeg',
            'Strawberry Ice Cream (2 Scoops)':    'https://img.pikbest.com/photo/20250425/delicious-strawberry-ice-cream-scoops-with-fresh-garnish_11678826.jpg!w700wp',
            'Strawberry Ice Cream (3 Scoops)':    'https://img.freepik.com/free-photo/strawberry-ice-cream-scoops_23-2149450703.jpg',
            'Chocolate Ice Cream (2 Scoops)':     'https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=800&q=90',
            'Chocolate Ice Cream (3 Scoops)':     'https://images.unsplash.com/photo-1551024506-0bccd828d307?w=800&q=90',
            'Pista Ice Cream (2 Scoops)':         'https://t4.ftcdn.net/jpg/19/32/21/31/360_F_1932213189_vUt2a50o6I2AV6u77SnPGaFqjWW0SC20.jpg',
            'Pista Ice Cream (3 Scoops)':         'https://static.vecteezy.com/system/resources/previews/061/800/602/large_2x/delicious-scoops-of-pistachio-ice-cream-topped-with-chopped-nuts-ready-to-eat-photo.jpg',
            'Butter Scotch Ice Cream (2 Scoops)': 'https://images.unsplash.com/photo-1570197788417-0e82375c9371?w=800&q=90',
            'Butter Scotch Ice Cream (3 Scoops)': 'https://images.unsplash.com/photo-1576506295286-5cda18df43e7?w=800&q=90',
            'Mango Ice Cream (2 Scoops)':         'https://png.pngtree.com/thumb_back/fh260/background/20251025/pngtree-a-refreshing-scoop-of-bright-orange-mango-ice-cream-in-clear-image_20003488.webp',
            'Mango Ice Cream (3 Scoops)':         'https://media.istockphoto.com/id/186769069/photo/apricot-ice-cream.jpg?s=612x612&w=0&k=20&c=LXSYAD7cdZMZxlLxIUek5ck4d4ZXerm88xAc34YZ3Zg=',
            'Black Currant Ice Cream (2 Scoops)': 'https://images.unsplash.com/photo-1551024506-0bccd828d307?w=800&q=90',
            'Black Currant Ice Cream (3 Scoops)': 'https://images.unsplash.com/photo-1563805042-7684c019e1cb?w=800&q=90',

            # Milk Shake
            'Vanilla Milk Shake':                 'https://t3.ftcdn.net/jpg/03/54/86/28/360_F_354862824_i80vqfhLcEvfnfHNq7vZUScCXeL73SFc.jpg',
            'Strawberry Milk Shake':              'https://c8.alamy.com/comp/PA21K8/strawberry-milk-shake-to-take-away-with-straw-on-a-dark-background-PA21K8.jpg',
            'Chocolate Milk Shake':               'https://images.unsplash.com/photo-1572490122747-3968b75cc699?w=800&q=90',
            'Pista Milk Shake':                   'https://images.unsplash.com/photo-1638176066666-ffb2f013c7dd?w=800&q=90',
            'Butter Scotch Milk Shake':           'https://entirelyelizabeth.com/wp-content/uploads/2022/10/IMG_3638.jpg',
            'Mango Milk Shake':                   'https://images.unsplash.com/photo-1546173159-315724a31696?w=800&q=90',
            'Pomegranate Milk Shake':             'https://images.unsplash.com/photo-1553361371-9b22f78e8b1d?w=800&q=90',
            'Banana Milk Shake':                  'https://media.istockphoto.com/id/1321518131/photo/banana-milkshake-with-choco-decorated-with-fruit-on-table-isolated.jpg?s=612x612&w=0&k=20&c=21HqbvfPWUaW3yQRrluT4gUcOk2Bk1ouOK_j4IDFLmA=',
            'Black Currant Milk Shake':           'https://img.freepik.com/premium-photo/black-currant-smoothie-with-honey-milk_220925-2956.jpg',

            # Falooda
            'Falooda':                            'https://mir-s3-cdn-cf.behance.net/project_modules/disp/b9c09558295129.59f7371854738.jpg',
            'SPL Falooda':                        'https://images.unsplash.com/photo-1544145945-f90425340c7e?w=800&q=90',

            # Moglee Spl Drink
            'Jil Jigara':                         'https://images.unsplash.com/photo-1621506289937-a8e4df240d0b?w=800&q=90',
            'Badam Milk':                         'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS3ADkAxZRsvGyJpAXNstqPF_RrRNu1sRVZmQ&s',
            'Rose Milk':                          'https://images.unsplash.com/photo-1622268348720-507f204d29b4?w=800&q=90',
            'Mint Mojito':                        'https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=800&q=90',
            'Blue Mojito':                        'https://images.unsplash.com/photo-1551782450-3939704166fc?w=800&q=90',
        }

        updated = 0
        not_found = []

        for name, url in item_images.items():
            count = MenuItem.objects.filter(name=name).update(image=url)
            if count > 0:
                updated += count
                self.stdout.write(self.style.SUCCESS(f'✅ {name}'))
            else:
                not_found.append(name)

        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS(f'Done! {updated} items updated.'))

        if not_found:
            self.stdout.write(self.style.WARNING(f'{len(not_found)} items not found in DB:'))
            for n in not_found:
                self.stdout.write(self.style.WARNING(f'  - {n}'))
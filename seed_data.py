import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fitness_hub.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from exercises.models import Exercise
from store.models import Product, Category
from inspiration.models import InspirationPost

# Seed Exercises
exercises_data = [
    {'name': 'Barbell Bench Press', 'description': 'The bench press is a compound exercise that builds mass and strength in the chest, shoulders, and triceps.', 'muscle_group': 'chest', 'difficulty': 'intermediate', 'instructions': '1. Lie flat on a bench with feet on the floor.\n2. Grip the barbell slightly wider than shoulder width.\n3. Unrack the bar and lower it to your chest.\n4. Press the bar back up to full arm extension.\n5. Repeat for the desired reps.', 'sets': 4, 'reps': '8-12'},
    {'name': 'Dumbbell Flyes', 'description': 'An isolation exercise that targets the chest muscles through a wide arc movement.', 'muscle_group': 'chest', 'difficulty': 'beginner', 'instructions': '1. Lie on a flat bench holding dumbbells above your chest.\n2. Lower the dumbbells out to the sides in a wide arc.\n3. Squeeze your chest to bring the dumbbells back together.', 'sets': 3, 'reps': '12-15'},
    {'name': 'Pull-ups', 'description': 'A bodyweight compound exercise that builds a wide, strong back and improves grip strength.', 'muscle_group': 'back', 'difficulty': 'intermediate', 'instructions': '1. Hang from a pull-up bar with palms facing away.\n2. Pull your body up until your chin is above the bar.\n3. Lower yourself back down with control.', 'sets': 4, 'reps': '8-10'},
    {'name': 'Barbell Rows', 'description': 'A compound back exercise that builds thickness and strength in the upper back.', 'muscle_group': 'back', 'difficulty': 'intermediate', 'instructions': '1. Bend at the hips with a slight knee bend, holding a barbell.\n2. Pull the barbell to your lower chest.\n3. Squeeze your shoulder blades together at the top.\n4. Lower with control.', 'sets': 4, 'reps': '8-12'},
    {'name': 'Overhead Press', 'description': 'A compound shoulder exercise that builds strong, round deltoids and improves upper body pressing strength.', 'muscle_group': 'shoulders', 'difficulty': 'intermediate', 'instructions': '1. Stand with feet shoulder width apart, holding a barbell at shoulder height.\n2. Press the barbell overhead until arms are fully extended.\n3. Lower back to shoulders with control.', 'sets': 4, 'reps': '8-10'},
    {'name': 'Barbell Curls', 'description': 'The classic bicep builder that adds mass and definition to the front of the upper arm.', 'muscle_group': 'biceps', 'difficulty': 'beginner', 'instructions': '1. Stand holding a barbell with an underhand grip.\n2. Curl the bar up by flexing your elbows.\n3. Squeeze at the top, then lower with control.', 'sets': 3, 'reps': '10-12'},
    {'name': 'Tricep Dips', 'description': 'A compound movement that heavily targets the triceps while also working the chest and shoulders.', 'muscle_group': 'triceps', 'difficulty': 'intermediate', 'instructions': '1. Support yourself on parallel bars with arms straight.\n2. Lower your body by bending your elbows.\n3. Push back up to the starting position.', 'sets': 3, 'reps': '10-12'},
    {'name': 'Barbell Squats', 'description': 'The king of all exercises. Squats build total body strength, especially in the legs and core.', 'muscle_group': 'legs', 'difficulty': 'intermediate', 'instructions': '1. Position a barbell on your upper back.\n2. Stand with feet shoulder width apart.\n3. Lower your body by bending knees and pushing hips back.\n4. Descend until thighs are parallel to the floor.\n5. Drive back up to standing.', 'sets': 4, 'reps': '8-12'},
    {'name': 'Romanian Deadlift', 'description': 'Targets the hamstrings and glutes through a hip hinge movement pattern.', 'muscle_group': 'legs', 'difficulty': 'intermediate', 'instructions': '1. Stand holding a barbell with an overhand grip.\n2. Hinge at the hips, pushing them backward.\n3. Lower the bar along your legs until you feel a stretch.\n4. Drive your hips forward to return to standing.', 'sets': 4, 'reps': '10-12'},
    {'name': 'Plank', 'description': 'An isometric core exercise that builds stability and endurance in the abdominal muscles.', 'muscle_group': 'core', 'difficulty': 'beginner', 'instructions': '1. Get into a forearm push-up position.\n2. Keep your body in a straight line from head to heels.\n3. Hold the position without letting your hips sag.', 'sets': 3, 'reps': '30-60 sec'},
    {'name': 'Mountain Climbers', 'description': 'A dynamic exercise that works the core while also providing a cardiovascular challenge.', 'muscle_group': 'cardio', 'difficulty': 'beginner', 'instructions': '1. Start in a push-up position.\n2. Drive one knee toward your chest.\n3. Quickly switch legs in a running motion.\n4. Keep your core tight throughout.', 'sets': 3, 'reps': '20-30'},
    {'name': 'Deadlift', 'description': 'A full body compound exercise that builds raw strength in the posterior chain, back, and grip.', 'muscle_group': 'full_body', 'difficulty': 'advanced', 'instructions': '1. Stand with feet hip width apart, barbell over mid-foot.\n2. Bend down and grip the bar just outside your knees.\n3. Keep your back flat and chest up.\n4. Drive through your heels to lift the bar.\n5. Lock out at the top with hips fully extended.', 'sets': 4, 'reps': '5-8'},
]

for data in exercises_data:
    Exercise.objects.get_or_create(name=data['name'], defaults=data)

# Seed Categories and Products
chest_cat, _ = Category.objects.get_or_create(name='Chest Equipment', description='Equipment for chest workouts')
protein_cat, _ = Category.objects.get_or_create(name='Supplements', description='Protein and supplements')
gear_cat, _ = Category.objects.get_or_create(name='Gym Gear', description='Apparel and accessories')
equip_cat, _ = Category.objects.get_or_create(name='Home Equipment', description='Equipment for home gyms')

products_data = [
    {'name': 'Adjustable Dumbbells Set', 'description': 'Premium adjustable dumbbells ranging from 5 to 52.5 lbs. Perfect for home workouts with quick weight changes.', 'price': 299.99, 'category': equip_cat, 'stock': 15, 'featured': True},
    {'name': 'Resistance Bands Kit', 'description': 'Set of 5 color-coded resistance bands with different tension levels. Great for warm-ups, rehabilitation, and full body workouts.', 'price': 29.99, 'category': equip_cat, 'stock': 50},
    {'name': 'Whey Protein Isolate', 'description': 'Pure whey protein isolate with 27g protein per serving. Low carb, no artificial sweeteners. Vanilla flavor.', 'price': 54.99, 'category': protein_cat, 'stock': 30, 'featured': True},
    {'name': 'Pre-Workout Formula', 'description': 'High energy pre-workout with caffeine, beta-alanine, and citrulline. Berry blast flavor for maximum performance.', 'price': 39.99, 'category': protein_cat, 'stock': 25},
    {'name': 'Lifting Gloves', 'description': 'Premium leather lifting gloves with wrist support and padded palms. Available in multiple sizes.', 'price': 24.99, 'category': gear_cat, 'stock': 40},
    {'name': 'Gym Bag - Sport', 'description': 'Large capacity gym bag with separate shoe compartment, water bottle holder, and padded shoulder straps.', 'price': 44.99, 'category': gear_cat, 'stock': 20, 'featured': True},
    {'name': 'Olympic Barbell', 'description': '7-foot Olympic barbell with 300 lb capacity. Chrome finish with knurled grip. Perfect for home or commercial gym.', 'price': 189.99, 'category': equip_cat, 'stock': 10},
    {'name': 'Creatine Monohydrate', 'description': 'Micronized creatine monohydrate powder. 5g per serving for improved strength, power, and muscle recovery.', 'price': 22.99, 'category': protein_cat, 'stock': 60},
    {'name': 'Yoga Mat Premium', 'description': 'Extra thick non-slip yoga mat with carrying strap. Eco-friendly material, perfect for yoga and floor exercises.', 'price': 34.99, 'category': equip_cat, 'stock': 35},
]

for data in products_data:
    Product.objects.get_or_create(name=data['name'], defaults=data)

# Seed Inspiration
inspiration_data = [
    {'title': 'The Only Bad Workout', 'quote': 'The only bad workout is the one that didn\'t happen.', 'author': 'Unknown', 'category': 'motivation'},
    {'title': 'Strength Comes From Within', 'quote': 'Strength does not come from physical capacity. It comes from an indomitable will.', 'author': 'Mahatma Gandhi', 'category': 'quote'},
    {'title': 'Consistency is Key', 'quote': 'It does not matter how slowly you go as long as you do not stop.', 'author': 'Confucius', 'category': 'quote'},
    {'title': 'Protein Timing Tip', 'quote': 'Consume 20-30g of protein within 30 minutes after your workout to maximize muscle protein synthesis and recovery.', 'author': 'Fitness Hub', 'category': 'tip'},
    {'title': 'Sleep & Recovery', 'quote': 'Muscles are built in the kitchen and the bedroom, not just the gym. Aim for 7-9 hours of quality sleep every night.', 'author': 'Fitness Hub', 'category': 'tip'},
    {'title': 'Mind Over Matter', 'quote': 'Your body can stand almost anything. It\'s your mind that you have to convince.', 'author': 'Andrew Murphy', 'category': 'motivation'},
]

for data in inspiration_data:
    InspirationPost.objects.get_or_create(title=data['title'], defaults=data)

print("Seed data created successfully!")

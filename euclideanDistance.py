import math

# Öklid mesafesi hesaplama fonksiyonu
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# 2D uzaydaki noktaları temsil eden noktalar listesi
points = [(1, 2), (4, 6), (5, 3), (9, 8)]

# Mesafeleri saklamak için bir liste
distances = []

# Her nokta çifti arasındaki mesafeyi hesaplama
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# Minimum mesafeyi bulma
min_distance = min(distances)

# Sonucu yazdırma
print("Points list:", points)
print("Distances list:", distances)
print("Minimum distance:", min_distance)

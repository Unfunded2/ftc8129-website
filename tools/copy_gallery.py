import shutil

source_files = [
    ('photos/IMG_20260116_223640_655.jpg', 'photos/gallery-1.jpg'),
    ('photos/event-photo.jpg', 'photos/gallery-2.jpg'),
    ('photos/team-photo.jpg', 'photos/gallery-3.jpg'),
]

for src, dst in source_files:
    try:
        shutil.copyfile(src, dst)
        print(f'Copied {src} -> {dst}')
    except Exception as e:
        print(f'Failed to copy {src} -> {dst}: {e}')

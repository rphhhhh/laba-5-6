def parse_line(line):
#Парсинг и валидация одной строки
    parts = line.strip().split()                     # разбиваем по пробелам
    if len(parts) != 5:                              # должно быть ровно 5 частей
        raise IndexError("list index out of range")
    ts = parts[0] + " " + parts[1]                   # timestamp = дата + время
    if len(ts) != 19:                                # длина строго 19 символов
        raise ValueError("Invalid timestamp length")
    temp = float(parts[3])                           # температура
    if not -50.0 <= temp <= 50.0:                    # диапазон -50..50
        raise ValueError(f"Temperature {temp} out of bounds [-50, 50]")
    hum = float(parts[4])                            # влажность
    if not 0.0 <= hum <= 100.0:                      # диапазон 0..100
        raise ValueError(f"Humidity {hum} out of bounds [0, 100]")
    return f"{parts[0]} * {parts[1]} * {parts[2]} * {temp} * {hum}"  # формат clean

def process_file(inp="iot_raw.txt", clean="iot_clean.txt", log="iot_log.txt"):
#Обработка файла с конструкцией try-except-else-finally
    valid, errors, total, success = [], [], 0, 0
    opened = False

    try:
        with open(inp, "r", encoding="utf-8") as f:  # только with, без .close()
            opened = True
            for i, line in enumerate(f, 1):          # построчное чтение (экономия RAM)
                total += 1
                if not line.strip(): continue
                try:
                    valid.append(parse_line(line))   # валидная строка
                    success += 1
                except (ValueError, IndexError) as e:
                    errors.append(f"[ОШИБКА] Строка {i}: {e}")  # битая в лог
    except FileNotFoundError:
        errors.append("[ОШИБКА] Входной файл не найден")
        print("Файл не найден")
    except Exception as e:
        errors.append(f"[ОШИБКА] Критическая: {e}")
    else:                                            # else только при успешном try
        if opened:
            with open(clean, "w", encoding="utf-8") as out:
                out.write("\n".join(valid) + ("\n" if valid else ""))
            print(f"Валидные → {clean}: {success} строк")
    finally:                                         # всегда пишем статистику
        stats = f"[СТАТИСТИКА] Обработано: {total}, Успешно: {success}, Ошибок: {total-success}"
        errors.append(stats)
        with open(log, "w", encoding="utf-8") as lg:
            lg.write("\n".join(errors) + "\n")
        print(stats)
        print("Обработка завершена")

if __name__ == "__main__":
    raw = """2023-10-25 10:00:00 S1 22.5 45.0
2023-10-25 10:00:05 S2 150.0 30.0
2023-10-25 S3 20.0 50.0
2023-10-25 10:00:10 S4 21.0 abc
"""
    with open("iot_raw.txt", "w", encoding="utf-8") as f:
        f.write(raw)
    process_file()